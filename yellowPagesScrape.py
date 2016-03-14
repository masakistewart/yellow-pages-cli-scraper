from bs4 import BeautifulSoup
import requests
from practice1 import getPhoneNumber
from sys import argv

def searchYellowP():
	term = argv[1]
	location = argv[2].split(" ")
	# query = "+".join(term.split(' '))
	r = requests.get('http://www.yellowpages.com/search?search_terms=' + str(term) + '&geo_location_terms='+ location[0] +'%2C+CA')
	soup = BeautifulSoup(r.content, "html5lib")
	htmlList = soup.find_all('div', {"class": "info"})
	for item in htmlList:
		if getPhoneNumber(item.text) is not None:
			companyName = item.find_all('h3', {'class': 'n'})
			print(getPhoneNumber(item.text).group(), companyName[0].text, term)



searchYellowP()
