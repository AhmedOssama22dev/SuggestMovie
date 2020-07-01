
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
l=list()
class Data():
	lst=list()
	def fetch_data(self,lst):

		# Ignore SSL certificate errors
		ctx = ssl.create_default_context()
		ctx.check_hostname = False
		ctx.verify_mode = ssl.CERT_NONE

		url="https://www.imdb.com/chart/top?ref_=nv_mv_250_6"
		html=urlopen(url,context=ctx).read()
		soup=BeautifulSoup(html,'html.parser')


		tags=soup('td',class_ = 'titleColumn') #this returns a tag so we wana process the tag text not the tag itself see the following for loop
		for tag in tags:
			#note: strip() remove a certain string/split() extract a certain string and remove the rest
			movie=tag.text.strip().replace('\n','').replace('      ','')
			rank=movie.split('.')[0]   #The split function returns a list of what before the delimeter and what's after it so we take the 0 index
			movie_name=movie.split('.')[1].split('(')[0]
			year=movie.split('(')[1].split(')')[0]
			lst.append([rank,movie_name,year])
		return lst
