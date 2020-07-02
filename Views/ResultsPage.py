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
		<body style="background:rgba(0,26,51,1)">
			<h1 style="text-align:center;color:white">We suggest,</h1>
			<p style="text-align:center;color:white;font-size:25"><em>{self.movie_name}</em></p>
			<p style="text-align:center;font-size:20">
				<img src='{self.link}' alt='This is the poster of {self.movie_name}' width="420" height="420">
			</p>
			<p style="text-align:center;color:white;font-size:20">
			YEAR={self.year}<br>RANK ON IMDb:{self.rank}
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
