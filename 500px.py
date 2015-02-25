#!/usr/bin/python3.3

from bs4 import BeautifulSoup
import urllib.request
import sys


def getSource(url):
    reponse = urllib.request.urlopen(url)
    pageSource = reponse.read()
   
    return BeautifulSoup(pageSource.decode("utf8"))

def getUrlImage(html):
	tag = html  .find('meta', attrs={'property' : 'og:image', 'content' : True })
	
	return tag['content']
	
def getImageTitle(html):
	tag = html.find('meta', attrs={'property' : 'og:title', 'content' : True})
	
	return tag['content']
	
def downloadImage(url):
	html = getSource(url)
	
	urlImage = getUrlImage(html)
	titleImage = getImageTitle(html) + ".jpg"
	
	urllib.request.urlretrieve(urlImage, titleImage)
	
def printUsage():
    print("Usage : " + sys.argv[0] + " [url]")
	
	
	
if __name__ == "__main__":
    
    if(len(sys.argv) == 2):
	    downloadImage(sys.argv[1])
    else:
	    printUsage()
	
