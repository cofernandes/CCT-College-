from urllib2 import urlopen
from bs4 import BeautifulSoup

print "enter a title"
title = raw_input()



cleaned = title.replace (" ", "_")
url = 'https://en.wilipedia.org/wiki/' + cleaned

print url

r = urlopen(url)
html_doc = str(r.read())


soup = BeautifulSoup(html_doc, 'html.parser')

#for each link insede of the soup
# find all the "a" tags and print out the href
for link in soup.find_all('a'):
    print link.get('href')