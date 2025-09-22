from perplexity import PerplexAPI

def main():
    api = PerplexAPI("perplex_api/driver/geckodriver")

    cookies = {
        'ph_phc_TXdpocbGVeZVm5VJmAsHTMrCofBQu3e0kN8HGMNGTVW_posthog': '%7B%22distinct_id%22%3A%2201996a11-64a2-7c4e-842e-4377b08bc9d8%22%2C%22%24sesid%22%3A%5B1758421170241%2C%2201996a11-64a2-7c4e-842e-4375f8b719f8%22%2C1758421148834%5D%7D',
        'pplx.visitor-id': 'e1bf7b6f-ade7-421e-8783-78079751954a',
        'gov-badge': '3',
        'AWSALB': '9yOz+qcu+btCaqNMaeG+QNs+3nnhcWhOquHp4lF0Z4bQt3qjll8sEUiHQ7iHAIbNsWeUZQkreiFFNPh5OngXmJs0dK/dQNKPKCmrYvPGKPCOWNL/ReJkX7vDk3pBvXtZSECfQFI3a1XFb8zR4t/qCwiR4WkyJanjgrh34veI3B9q2so+rT/NHfXo+V0VWQ==',
        'AWSALBCORS': '9yOz+qcu+btCaqNMaeG+QNs+3nnhcWhOquHp4lF0Z4bQt3qjll8sEUiHQ7iHAIbNsWeUZQkreiFFNPh5OngXmJs0dK/dQNKPKCmrYvPGKPCOWNL/ReJkX7vDk3pBvXtZSECfQFI3a1XFb8zR4t/qCwiR4WkyJanjgrh34veI3B9q2so+rT/NHfXo+V0VWQ==',
        '__cflb': '02DiuDyvFMmK5p9jVbVnMNSKYZhUL9aGm15RLVzvkz4Cc',
        'sidebarHiddenHubs': '[]',
        'cf_clearance': 'V7YX0BwzhWAXbzIE3Z1CyESorgcUjU5HzTaDCexdgQc-1758436984-1.2.1.1-fYeclXy.OTid6iqO7ETScnuOV7FFSo.OH3LQWX8uDbMFrQdGnPzCpBWEZC_it8Ke0krtxkwtxIUVPIH0xK7c2pQuuqaPFttCT4IQwHCpT1SwOoS7EVvn7YbseG58z5eddDAbgkTnpQA0ZCWrqXgytGyLTJrWI4ep_0vSt0e7tIhGRJmvyst_N5WM8mWPSQvmgafwH.SQw8yIyLupZHH1.ShhBtHERbNNZA1P5JFBDpo',
        '__stripe_mid': '9ed5246e-eb3d-4176-853a-863ba16537107be564',
        '__Secure-next-auth.session-token': 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..RLFMa38bx_wZWpPJ.9mj7Xhx6eZqzGEHBxUw270DByczIlL1uTU5LPPuCTAn7hmFhweaD1TDY2TA2TgZs5lNi5XuA4969JrFcIVyHylcObXZzIhC4lqxvbRoM_l7eQ72y-suLAlMfX4a1M3z9y3YsoaxA1SKvE07aKzXIm1WPsmo4ZWJqyNxN2OeGfX8ga7NKyazlp4OK06t8KYIBmo68Vf1_7XURhl0m6jL1tI55hnmo8-ksSDnjZYyKq4B6ht6OKzjrNKW7xZks_cz65jA3dJraQTv9QKQHlgfSsuhwYHyeAvDzqOf8Zn78YSlhtR0Wo9ZfN5XG3kAShIPUZrMxA4rAr0joWexsIFbbLYxTmbfzVRDp9LdB9mYmpiOL8s9x5gXOarChLg4lUOsaYkFAuVpTKXN-4w6FKhDByzcsIBelUyTSwiJftFM.0bKxshpMUkvTp9qVAj5TRQ',
        'pplx.metadata': '{%22qc%22:23%2C%22qcu%22:0%2C%22qcm%22:0%2C%22qcc%22:0%2C%22qcco%22:0%2C%22qccol%22:0%2C%22qcdr%22:0%2C%22qcs%22:0%2C%22qcd%22:0%2C%22hli%22:true%2C%22hcga%22:true%2C%22hcds%22:false%2C%22hso%22:false%2C%22hfo%22:false%2C%22hsco%22:false%2C%22hfco%22:false%2C%22hsma%22:false%2C%22fqa%22:1758421615011%2C%22lqa%22:1758441580885}',
        'pplx.personal-search-badge-seen': '{%22sidebar%22:true%2C%22settingsSidebar%22:false%2C%22personalize%22:false}',
        'pplx.search-mode': 'search',
        'pplx.session-id': 'ac579854-9f50-43ad-9ecb-5d63aaeddc19',
        '_dd_s': 'aid=0cf3037c-03f5-4a46-8155-0a03192e2246&rum=2&id=63554ba8-6bdd-42e5-ab22-9974db9f7408&created=1758462465241&expire=1758463376999&logs=0',
        '__cf_bm': 'lX_QVpPDoWMt_9XNZwXxngg3ls8ESppdnbc6KaL73Y4-1758462465-1.0.1.1-fm5xazg6jU0qBtEHoYkQJwZL7uxA9n7uz.2mF7jkFTB5rs.uIcUShhoqsP.32WMVDprgyhOX6N49DnD88V609wec2kfX7h7CkzcHZeLKBIk',
        'next-auth.csrf-token': 'a32243d6e396f9cf7c7a3d1032e077cc395e42551c1d45ed188c71d22a3531ac%7C53eeabfc333536cf0e3459314c939d711d2a5e037a5e08a676a51c92b60bcf0e',
        'next-auth.callback-url': 'https%3A%2F%2Fwww.perplexity.ai',
        '__stripe_sid': 'd8350ea0-47d8-452f-b001-00fd0cb81155d57fdd',
    }

    with api:
        # First, navigate to the site
        api.get_data("https://www.perplexity.ai/")
        
        # Then set the cookies
        api._set_cookies(cookies)
        
        # Now perform the search
        result = api.search("how are you doing today?")
        print(result)

if __name__ == "__main__":
    main()