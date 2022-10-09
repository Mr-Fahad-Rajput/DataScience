import requests
from bs4 import BeautifulSoup
import re

site = requests.get('https://entertainment.time.com/2005/10/16/all-time-100-novels/slide/all/')
soup = BeautifulSoup(site.content, 'html.parser')

#links Extraction
completeList = soup.find( class_ = "entry-content group")
listItems = (completeList.find_all('li'))
links = []
for link in completeList.findAll('a'):
    links.append(link.get('href'))

links.pop(0)
links.pop()
links.pop() #Links Finalized


linkString = ",".join(str(x) for x in links)



linksCleaned = re.sub(',' , '   ', linkString)
linksCleaned = re.sub('/' , '_', linksCleaned)
linksCleaned = re.sub('-' , '_', linksCleaned)


usableData = re.findall('_slide_\w+', linksCleaned)
usableData = ",".join(str(x) for x in usableData) # Have to convert Each Result to a string to perform regex Searches

#Date Extraction
dates = re.findall('\d+', usableData) # All Dates Finalized

#Extracting Author Names
authorNames = re.findall('_by_\w+', usableData)
authorNames = ",".join(str(x) for x in authorNames) 
authorNames = re.sub('_by_' , ' ', authorNames)
authorNames = re.findall('\w+' ,authorNames)
authorNames = ",".join(str(x) for x in authorNames) 
authorNames = re.sub('_' , ' ', authorNames)
authorNames = re.split(',' ,authorNames)
authorNames = [authorName.title() for authorName in authorNames] # Authors Names Finalized

# Extracting Names Of Books
bookNames = re.findall('ide_\w+_by_', usableData)
bookNames = ",".join(str(x) for x in bookNames) 
bookNames = re.sub('_by_' , ' ', bookNames)
bookNames = re.sub('\d' , ' ', bookNames)
bookNames = re.sub('ide_' , ' ', bookNames)
bookNames = re.sub('_' , ' ', bookNames)
bookNames = re.sub('\s+' , ' ', bookNames)
bookNames = re.split(',' ,bookNames)
bookNames = [bookName.title() for bookName in bookNames] # Book Names Finalized




print(bookNames, authorNames, dates)


