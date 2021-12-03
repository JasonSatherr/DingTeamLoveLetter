import requests
#https://quotes.rest/
#https://theysaidso.com/api/#python
class QuoteAPI:
    def __init__(self, category = 'love') -> None:
        self.url = 'https://quotes.rest/qod?category=' + category
        self.headers = {'content-type': 'application/json'}
    def getQuoteJSON(self):
        response = requests.get(self.url, headers=self.headers)
        quotes=response.json()['contents']['quotes'][0]
        return quotes
        #print(quotes)


#print(response)

