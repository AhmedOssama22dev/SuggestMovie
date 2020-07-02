from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
class Image():
	images=dict()
	def fetch_image(self,images):
		ctx = ssl.create_default_context()
		ctx.check_hostname = False
		ctx.verify_mode = ssl.CERT_NONE

		url="https://www.imdb.com/chart/top?ref_=nv_mv_250_6"
		html=urlopen(url,context=ctx).read()
		soup=BeautifulSoup(html,'html.parser')
		#tags=soup('td',class_ = 'posterColumn')
		tags=soup('img')
		for tag in tags:
			movie=tag.get('alt',None)
			link=tag.get('src',None).replace('.jpg','')
			images[movie]=link
		return images