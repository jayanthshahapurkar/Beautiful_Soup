import requests
from bs4 import BeautifulSoup

result = requests.get("https://www.whitehouse.gov/briefings-statements/")
print (result.status_code)

scr = result.content

soup = BeautifulSoup(scr,'lxml')
url = []
for h2_tag in soup.find_all("h2") :
	a_tag = h2_tag.find('a')
	url.append(a_tag.attrs['href'])


print (url)

