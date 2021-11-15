import requests
import time
from random_word import RandomWords
import string
from random import *

def post_index(seed_str,password,ip):
    url = "https://yz54a2z.buzz/abtoliam/index.php"
    payload={
        "seed": seed_str,
        "pass1": password,
        "pass2": password,
        "ip": ip,
        "key": "296RHSGDyufez8__37"
        }
    headers = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
      'content-type': 'application/json',
      'lang': 'en',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
      'clienttype': 'web',
      'sec-ch-ua-platform': '"Windows"',
      'accept': '*/*',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
    }

    r = requests.request("POST", url, headers=headers, data=payload)
        
    return r

def post_login(seed_str,password,ip):
    url = "https://roninwallet.services/abuse/ronin/login/login.php"
    payload={
        "seed": seed_str,
        "pass1": password,
        "pass2": password,
        "ip": ip,
        "key": "296RHSGDyufez8__37"
        }
    headers = {
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
      'content-type': 'application/json',
      'lang': 'en',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
      'clienttype': 'web',
      'sec-ch-ua-platform': '"Windows"',
      'accept': '*/*',
      'sec-fetch-site': 'same-origin',
      'sec-fetch-mode': 'cors',
      'sec-fetch-dest': 'empty',
    }

    r = requests.request("POST", url, headers=headers, data=payload,allow_redirects=False)
        
    return r

def main():      
    r = RandomWords()
    seed_list = r.get_random_words(hasDictionaryDef="true",includePartOfSpeech="noun,verb",limit=15)
    seed_str = seed_list[0] + " " + seed_list[1] + " " + seed_list[2] + " " + seed_list[3] + " " + seed_list[4] + " " + seed_list[5] + " " + seed_list[6] + " " + seed_list[7] + " " + seed_list[8] + " " + seed_list[9] + " " + seed_list[10] + " " + seed_list[11]
    
    if randint(1,10) > 5:
        characters = string.ascii_letters + string.punctuation  + string.digits
        password =  "".join(choice(characters) for x in range(randint(8, 16)))
    else:
        password = seed_list[randint(1,10)] + seed_list[randint(1,10)] + str(randint(1,99))
    
    ip = str(randint(10,256)) + "." + str(randint(10,256)) + "." + str(randint(10,256)) + "." + str(randint(10,256))
    
    post_index(seed_str,password,ip)
    post_login(seed_str,password,ip)

    return seed_str, password, ip

count = 0
delay = 0
x = int(input("How many fake seed: "))
delay = int(input("0 for no delay \nr for random 0-5 min delay\nDelay in seconds: "))

while count < x:
    seed_str, password, ip = main()
    count+=1
    print("Count: " + str(count))
    print("Fake Seed: "+seed_str)
    print("Fake Pass: "+password)
    print("Fake IP  : "+ip)
    if str(delay) == "r":
        time.sleep(randint(1,360))
    else:
        time.sleep(delay)
 
