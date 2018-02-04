# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*-
import requests, sys, bs4
reload(sys)
import locale
sys.setdefaultencoding(locale.getpreferredencoding())
from bs4.element import Comment
import urllib
from collections import Counter

#prints link content in text 
def BSprint(url):
	try:
		out_text= urllib.request.urlopen(url).read()
	except HTTPError as e:

		return None
	soup = bs4.BeautifulSoup(out_text,"lxml")
	# kill all script and style elements
	for script in soup(["script", "style"]):
	    script.extract()    
	# rip it out	
	# get text
	text = soup.get_text()	
	# break into lines and remove leading and trailing space on each
	lines = (line.strip() for line in text.splitlines())
	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# drop blank lines
	text = '\n'.join(chunk for chunk in chunks if chunk)
	#print(text.encode('utf-8'))
	return text
	
#returns list of links web search word
def linkListSearch(animal):
	print('Googling...') # display text while downloading the Google page
	reqOut='http://google.com/search?q=' + ' '.join(animal)
	print("request>>>>"+reqOut)
	res = requests.get(reqOut)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text,"lxml")
	linkElems = soup.select('.r a')
	bad=["youtube","twitter"]
	resultList=[]
	wrongLinks=[]
	for i in range(len(linkElems)):
		address='http://google.com' + linkElems[i].get('href')
		if "q=http" in  address:
			resultList.append(address)
	#collect links,containing twitter,youtube
	for addr in resultList:
		if any(ext in addr for ext in bad):
			wrongLinks.append(addr)
	#removes twitter from set of links
	gL=set(resultList)
	bL=set(wrongLinks)
	rL=gL-bL
	finalList=list(rL)
	print(finalList)
	return finalList

if __name__ == "__main__":
	listItems=["враги"]
	#generates google list of links
	finList=linkListSearch(listItems)
	for testPrint in finList:
		print("googleReqe>>>>>"+testPrint)
	#takes the links one by one and text
		fin=BSprint(testPrint)
	#splits text and gives words number
		counter = Counter(fin.strip().split())
		for pri in counter.most_common(40):
			if len(pri[0])>3:
				print(">>>>>>"+str(pri))
				
