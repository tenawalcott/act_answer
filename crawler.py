import requests
from lxml import etree
import re
from bs4 import BeautifulSoup
import time
import datetime

real_start = time.time()
r = requests.get("http://www.actmi.net/")
e = etree.HTML(r.text)
for i in range(1, 62):
    print(i)
    try:
        start = time.time()
        k = etree.tostring(e.xpath('//*[@id="atable"]/tbody/tr[{}]/td[2]/a'.format(i))[0])
        pattern = r'./[a-z]+/[0-9a-z]+/[a-z]+'
        k = re.findall(pattern, str(k))
        k = re.split('/', k[0])
        num = k[2]
        new = "http://www.actmi.net/downloads/" + num + "/answers"
        r = requests.get(new)
        r.encoding = "utf-8"
        soup = BeautifulSoup(r.text, "html.parser")
        k = soup.select('body > div.container.mt-100.mb-60 > div > div > table > tbody > tr:nth-child(75) > td:nth-child(2) > a')
        ex = k[0].get('data-content')
        name = num+".txt"
        with open(name, "w", encoding="utf-8") as f:
            f.writelines(str(num)+"\n")
            f.writelines("English"+"\n")
            for j in range(1, 76):
                k = soup.select(
                    "body > div.container.mt-100.mb-60 > div > div > table > tbody > tr:nth-child({}) > td:nth-child(2) > a".format(
                        j))
                k = k[0]
                ex = k.get('data-content')
                f.writelines(str(j)+".\n")
                f.writelines(str(k.get_text())+"\n")
                f.writelines(str(ex)+"\n")
                f.writelines("\n")
            f.writelines("Math" + "\n")
            for j in range(1, 61):
                k = soup.select(
                    "body > div.container.mt-100.mb-60 > div > div > table > tbody > tr:nth-child({}) > td:nth-child(3) > a".format(
                        j))
                k = k[0]
                ex = k.get('data-content')
                f.writelines(str(j) + ".\n")
                f.writelines(str(k.get_text()) + "\n")
                f.writelines(str(ex) + "\n")
                f.writelines("\n")
            f.writelines("Reading" + "\n")
            for j in range(1, 41):
                k = soup.select(
                    "body > div.container.mt-100.mb-60 > div > div > table > tbody > tr:nth-child({}) > td:nth-child(4) > a".format(
                        j))
                k = k[0]
                ex = k.get('data-content')
                f.writelines(str(j) + ".\n")
                f.writelines(str(k.get_text()) + "\n")
                f.writelines(str(ex) + "\n")
                f.writelines("\n")
            f.writelines("Science" + "\n")
            for j in range(1, 41):
                k = soup.select(
                    "body > div.container.mt-100.mb-60 > div > div > table > tbody > tr:nth-child({}) > td:nth-child(5) > a".format(
                        j))
                k = k[0]
                ex = k.get('data-content')
                f.writelines(str(j) + ".\n")
                f.writelines(str(k.get_text()) + "\n")
                f.writelines(str(ex) + "\n")
                f.writelines("\n")
        print(time.time()-start)
        time.sleep(5)
    except:
        print("false")
        continue
print(time.time()-real_start)
