import sys
import requests
from bs4 import BeautifulSoup

# first arg == script name ?
if len(sys.argv) != 3:
  print "Please provide 2 fighter names"
  sys.exit()

queryTerms = [sys.argv[1].lower(), sys.argv[2].lower(), "fight", "video"]
query = "+".join(queryTerms)
  
response = requests.get("http://mmaversus.com/?s=" + query)
soup = BeautifulSoup(response.text, 'html.parser')

firstUrl = None
for link in soup.find_all('a'):
  url = link.get('href').lower()
  if all(str in url for str in queryTerms):
    firstUrl = link.get('href')
    break
    
if firstUrl == None:
  print "Couldn't find video"
    
response = requests.get(firstUrl)
soup = BeautifulSoup(response.text, 'html.parser')

desiredUrl = None
for link in soup.find_all('a'):
  if 'Dedi.Blog' in link.getText():
    desiredUrl = link.get('href')
    
if desiredUrl == None:
  print "Couldn't find video"
    
sys.stdout.write(desiredUrl)
sys.stdout.flush()
sys.exit(0)