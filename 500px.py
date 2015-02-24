from bs4 import BeautifulSoup
import urllib.request
import sys


def getSource(url):
    reponse = urllib.request.urlopen(url)
    pageSource = reponse.read()
   
    return BeautifulSoup(pageSource.decode("utf8"))

def getUrlImage(html):
	tag = hmtl.find('meta', attrs={'property' : 'og:image', 'content' : True })
	
	return tag['content']
	
def getImageTitle(html):
	tag = html.find('meta', attrs={'property' : 'og:title', 'content' : True})
	
	return tag['content']
	
def downloadImage(url):
	html = getSource(url)
	
	urlImage = getUrlImage(html)
	titleImage = getImageTitle(html)
	
	request.urlretrieve(urlImage, titleImage)
	
	
	
if __name__ == "__main__":
	downloadImage(sys.argv[1])
	