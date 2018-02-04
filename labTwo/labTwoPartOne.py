import random
import webbrowser

websites=["https://www.twitter.com","https://www.google.com","https://www.facebook.com","https://www.masrawy.com","https://www.python.org/","https://www.w3schools.com/"]

def openWebsite():
    x=(random.choice(websites))
    webbrowser.open_new(x)

openWebsite()
