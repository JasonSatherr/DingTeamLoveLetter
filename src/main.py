import sys
sys.path.append(".")
from QuoteAPI import QuoteAPI
from twilo import TwiloAPI
import random
from datetime import date
import calendar

def main():
    print("herro andy.")
    loveQuote = QuoteAPI()  #loveQuote is an object of QuoteAPI
    quoteJSON = loveQuote.getQuoteJSON()    #quoteJSON is now the love quote of the day
    print(quoteJSON)

    #get love quote
    loveQuoteStr = quoteJSON['quote']

    #get nickname
    nicknames = ['pumpkin pie', 'tutu', 'tu', 'my love', 'my dearest', 'my little big planet', 'my happy',\
        'my sweet', 'my creampuff', 'my baby doll', 'my sweet tea', 'my sweet', 'my  goofball', 'my darling',\
            'my lovely', 'my joy', 'my sugar mommy', 'my MOMMMY', 'silly head', '4head', 'silly goose',\
                'my matcha', 'two', 'my girlfriend, tu']  #move this to a csv in the future
    chosenNickname = random.choice(nicknames)

    #get day
    curr_date = date.today()
    day = (calendar.day_name[curr_date.weekday()])

    message = "\nGood " + str(day) + " " + str(chosenNickname) + "!\nHere\'s your daily love quote,\n\n" \
    + "\"" + str(loveQuoteStr) + "\""
    twilo = TwiloAPI()
    twilo.sendMessage(message)


    #print the love quote of the day for me you will have to dig through the JSON to get it
    #If you're really ambitious you can also grab the author and toy with printing it as...
    #"If you really wanna be a rockstar, just rock out"
    #                                     -Jason

if __name__ == "__main__":
    main()