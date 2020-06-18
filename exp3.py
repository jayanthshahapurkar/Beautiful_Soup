from bs4 import BeautifulSoup


# To keep things simple and also reproducible, consider the following HTML code
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; their names:
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
<b class="boldest">Extremely bold</b>
<blockquote class="boldest">Extremely bold</blockquote>
<b id="1">Test 1</b>
<b another-attribute="1" id="verybold">Test 2</b>
"""
with open ('index.html','w') as file :
	file.write(html_doc)

soup = BeautifulSoup(html_doc,"lxml")

#print (soup)
#print(soup.prettify())


print(soup.b)


print(soup.find('p'))


print (soup.find_all('b'))


print(soup.b.name)


tag = soup.b

print(tag)


tag.name = "blockquote"

print (tag)




#Attributes:


tag = soup.find_all('b')[2]
print (tag)



print(tag['id'])

#tag = soup.find_all('b')[3]
print(tag)


print(tag['id'])
print(tag['another-attribute'])


tag = soup.find_all('b')[3]
print(tag)

print(tag.attrs)


print(tag)
tag['another-attribute'] = 2
print(tag)


del tag['id']
del tag['another-attribute']
print(tag)

# Multi-valued Attributes
tag = soup.find_all('b')[3]
print(tag)
print(tag.string)

# We can use the "replace_with" function to replace
# the content of the string with something different:
tag.string.replace_with("This is another string")
print(tag)

