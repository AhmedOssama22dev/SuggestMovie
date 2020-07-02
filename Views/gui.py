import tkinter as tk
import tkinter.font as tkFont
from urllib.request import urlopen
import webbrowser
from ResultsPage import results
from topMovieList import Data
from randomMovie import Suggest
from Poster import Image
#
movies_lst=list()
suggested_movie=list()
data=Data()
data.fetch_data(movies_lst)
suggest=Suggest()
suggested_movie= suggest.randomize(movies_lst)

images=dict()
image=Image()
images=image.fetch_image(images)
print(images[suggested_movie[1]])
#randomize(fetch_data) => returns a list from the movies_lst
html=''
results=results(suggested_movie[1],suggested_movie[2],suggested_movie[0],images[suggested_movie[1]],html)

class window(tk.Tk):
	def __init__(self):
		super().__init__()
		#Setting up window style:
		self.title('Movie suggestions')
		self.resizable(False,False)
		#Centering the window on the screen:
		# Gets the requested values of the height and widht.
		windowWidth = self.winfo_reqwidth()
		windowHeight = self.winfo_reqheight()

		# Gets both half the screen width/height and window width/height
		positionRight = int(self.winfo_screenwidth()/2 - windowWidth/2)
		positionDown = int(self.winfo_screenheight()/2 - windowHeight/2)

		# Positions the window in the center of the page.
		self.geometry("+{}+{}".format(positionRight, positionDown))


		#Setting up gadgets:
			#Setting up Fonts:
		lbl_font_style=tkFont.Font(family="Lucida Grande",size=20)
		btn_font_style=tkFont.Font(family="Lucida Grande",size=10)
		
		label=tk.Label(self,text='Click the button to shuffle movies :)',font=lbl_font_style)
		label.grid(row=0,column=50,rowspan=5,sticky='e')
		shuffle_btn=tk.Button(self,text='SHUFFLE',font=btn_font_style,command=results.open_html) #if we put the paranth. it will launch the function automatically
		shuffle_btn.grid(row=6,column=50)


if __name__=="__main__":
	window=window()
	window.mainloop()

