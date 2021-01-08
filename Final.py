import os
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}
r1 = requests.get('https://www.lttstore.com/collections/all', headers=headers)
r2 = requests.get('https://www.lttstore.com/collections/all?page=2', headers=headers)
r1 = r1.text
r2 = r2.text
r1 = r1.split('"')
r2 = r2.split('"')

website_everything_before = r1 + r2
href_products_before = []
for x in website_everything_before:
    if "/collections/all/products/" in x:
        href_products_before.append(x)
    else:
        pass

while True:
    r111 = requests.get('https://www.lttstore.com/collections/all', headers=headers)
    r222 = requests.get('https://www.lttstore.com/collections/all?page=2', headers=headers)
    r11 = r111.text
    r22 = r222.text
    r11 = r11.split('"')
    r22 = r22.split('"')
    website_everything_after = r11 + r22
    href_products_after = []
    for x in website_everything_after:
        if "/collections/all/products/" in x:
            href_products_after.append(x)
        else:
            pass
    for (after, before) in zip(href_products_after,href_products_before):
        if after != before:
            os.system("start https://www.lttstore.com" + after)
            exit()
        else:
            print(after,before)
            pass
    print(r111,r222)
    print("no diff found sleeping for 5 seconds")
    time.sleep(5)











