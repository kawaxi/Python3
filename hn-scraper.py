# pip3 install beutifulsoup4
# pip3 install requests

# Just a simple data scraper for hacker news

import requests
import pprint
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')

#print (res)
#print (res.txt)
#print(soup)
#print(soup.body)
#print(soup.body.contents)

# Gets all the links in a list.
#print(soup.find_all('a'))        

#print(soup.find_all('div'))

#print(soup.title) gets the title of the page

#gets the first ocurrence 
#print(soup.find('a'))  

soupobj= BeautifulSoup(res.txt, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.sbutext')

def create_custom_hn(links, subtext):

	hn = []
	for idx, item in enumerate(links):
		title = links[idx].getText()
		href = links[idx].get('href, None')
		vote = subtext[idx].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace('points,''))
			if points > 99:
				hn.append('{title': title, 'link': href, 'votes':points})
			
return hn

pprint.pprint(create_custom_hn(links,subtext))
