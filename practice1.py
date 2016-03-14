import requests
from bs4 import BeautifulSoup
import re


def getPhoneNumber(stringy):
	phoneNumberRegex = re.compile(r'''(
		(\d{3}|\(\d{3}\))?                # area code
	    (\s|-|\.)?                        # separator
	    (\d{3})                           # first 3 digits
	    (\s|-|\.)                         # separator
	    (\d{4})                           # last 4 digits
	    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
		)''', re.VERBOSE)
	stuff = re.search(phoneNumberRegex , stringy)
	return stuff

r = requests.get("http://www.yellowpages.com/search?search_terms=muaythai&geo_location_terms=Los+Angeles%2C+CA")
soup = BeautifulSoup(r.content, 'html5lib')
arr = soup.find_all('div', {"class": "info"})

# for thing in arr:
# 	nameText = thing.find_all('h3', {"class": "n"})
# 	if getPhoneNumber(thing.text) is not None:
# 		print(getPhoneNumber(thing.text).group(), nameText[0].text)