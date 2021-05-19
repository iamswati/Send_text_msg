# The requests module allows you to send HTTP requests using Python.
import requests
# The full-form of JSON is JavaScript Object Notation. ... Python supports JSON through a built-in package called json . To use this feature, we import the json package in Python script. The text in JSON is done through quoted string which contains the value in key-value mapping within { }
import json



# Takes two parameters: number and message
def send_sms(number, message):
    url = 'https://www.fast2sms.com/dev/bulk'
    params = {
        'authorization': 'jOP7Zf6c5xVBGyXLpz83RMKuleJFhUCwnvItQm29YDEbHkrS4inmrYWgRyFwHPOpvoBduNfesGCXQ2k0',
        'sender_id': 'FSTSMS',
        'message': message,
        'language': 'english',
        'route': 'p',
        'numbers': number
    }

    response = requests.get(url, params=params)
    dic = response.json()
    print(dic)


send_sms("9306979702", "Hy ..")
