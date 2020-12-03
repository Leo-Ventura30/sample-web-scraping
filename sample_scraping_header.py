import requests

proxies = {"http":"144.22.7.127:80"}
headers = {"user-agent":"Mozzila/5.0 (X1; Linux i686; rv:64.0) Gecko/20100101 Firefox/64.0"}

r = requests.get("https://login.flvs.net/", proxies=proxies, headers=headers)
print(r.text)
r.cookies=[['hittin'],['realet']]
for cookie in r.cookies:
    print(cookie)
