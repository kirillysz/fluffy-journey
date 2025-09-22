from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class PerplexAPI:
    def __init__(self, path_to_driver: str):
        self.path_to_driver = path_to_driver
        self.driver = webdriver.Firefox(service=Service(executable_path=path_to_driver))
        self.cookies = {}

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.driver:
            self.driver.quit()

    def _set_cookies(self, cookies: dict):
        self.cookies.update(cookies)
        
        for name, value in self.cookies.items():
            self.driver.add_cookie({"name": name, "value": value})

        self.driver.refresh()

    def get_data(self, url: str, timeout: int = 10) -> str:
        try:
            self.driver.get(url)
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
        except TimeoutError:
            print(f"Timeout waiting for page to load: {url}")
            raise

    def search(self, query: str, timeout: int = 10) -> str:
        self.get_data("https://perplexity.ai")
        print("дата получена")
        try:
            search_input = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.ID, "ask-input"))
            )
            print("нашел")
            search_input.send_keys(query)
            print("отправил")
            search_input.submit()

            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "prose text-pretty dark:prose-invert inline leading-relaxed break-words min-w-0 [word-break:break-word] prose-strong:font-medium"))
            )

            return self.driver.page_source
        
        except TimeoutError:
            print(f"Timeout waiting for search results: {query}")
            raise