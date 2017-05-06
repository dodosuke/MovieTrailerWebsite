import webbrowser as wb

#Difining the class Movie
class Movie():
	def __init__(self, movie_title, poster, trailerLink):
		self.title = movie_title
		self.poster_image_url = poster
		self.trailer_youtube_url = trailerLink

	def show_trailer(self):
		wb.open(self.trailer)
