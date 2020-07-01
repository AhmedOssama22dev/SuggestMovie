#this class to modify the html using attributes given

from urllib.request import urlopen
import webbrowser
class results:
	def __init__(self,movie_name,year,rank,link,html):
		self.movie_name=movie_name
		self.year=year
		self.rank=rank
		self.link=link
		self.html=f'''
		<html>
		<head>
			<title>results</title>
		</head>
		<body>
			<h1>We recommend,{self.movie_name}</h1>
			<p>
				<img src='https://placebear.com/200/300' alt='This is the poster of {self.movie_name}'>
			</p>
			<p>
			Year={self.year}<br>Rank={self.rank}<br><a href={self.link}>Check on IMBD</a>
			</p>
		</body>
		</html>
		'''

		f=open('results.html','w')
		f.write(self.html)
		f.close()
	def open_html(self):
		new =2
		url = "results.html"
		webbrowser.open(url,new=new)
