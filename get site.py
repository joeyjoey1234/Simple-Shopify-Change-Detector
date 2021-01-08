import requests
import os
import time
###  https://www.lttstore.com/collections/all?page=2
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}
r1 = requests.get('https://www.lttstore.com/collections/all',headers=headers)
r2 = requests.get('https://www.lttstore.com/collections/all?page=2',headers=headers)
r3 = requests.get("https://www.lttstore.com/",headers=headers)
r1 = r1.text
r2 = r2.text
r3 = r3.text
i = 0
keywords = ["3080","RTX","$1.00","$0.98","GPU"]

while i <= 10:
    r111 = requests.get('https://www.lttstore.com/collections/all',headers=headers)
    r222 = requests.get('https://www.lttstore.com/collections/all?page=2',headers=headers)
    r333 = requests.get("https://www.lttstore.com/",headers=headers)
    r11 = r111.text
    r22 = r222.text
    r33 = r333.text
    print(r11)
    print(r22)
    for x in keywords:
        if x in r11:

            os.system("start https://www.lttstore.com/collections/all")
            print("Starting Chrome3")
            exit()
        elif x in r22:
            os.system("start https://www.lttstore.com/collections/all")
            print("Starting Chrome3")
            exit()
        else:
            print(r111)
            print(r222)
            print("Passing and sleeping for 5 Seconds")
            pass

    time.sleep(5)


