import requests
from bs4 import BeautifulSoup


request = requests.get("https://www.google.com/")
print (request.status_code)
#print(request.headers)
scr = request.content
print ()
#print (scr)
soup = BeautifulSoup(scr,'lxml')
links = soup.find_all("a")
#print (links)
for link in links:
	print(links)
	print(link.attrs['href'])

