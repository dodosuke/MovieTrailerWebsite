import media
import fresh_tomatoes

zootopia = media.Movie("Zootopia", 
						"https://upload.wikimedia.org/wikipedia/en/e/ea/Zootopia.jpg",
						"https://www.youtube.com/watch?v=g9lmhBYB11U")
exmachina = media.Movie("Ex Machina",
						"http://kingink.biz/wp-content/uploads/2015/06/ex-machina-poster-v02.jpg",
						"https://www.youtube.com/watch?v=EoQuVnKhxaM")
madmaxfr = media.Movie("Mad Max Fury Road",
						"https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg",
						"https://www.youtube.com/watch?v=YWNWi-ZWL3c")
gattaca = media.Movie("Gattaca",
						"https://upload.wikimedia.org/wikipedia/en/b/bb/Gataca_Movie_Poster_B.jpg",
						"https://www.youtube.com/watch?v=hWjlUj7Czlk")
shaunofthedead = media.Movie("Shaun of the Dead",
						"https://images-na.ssl-images-amazon.com/images/M/MV5BMTU2NjA0NDk0NV5BMl5BanBnXkFtZTcwOTA0OTQzMw@@._V1_SY1000_CR0,0,621,1000_AL_.jpg",
						"https://www.youtube.com/watch?v=LIfcaZ4pC-4")
apartment = media.Movie("The Apartment", 
						"https://upload.wikimedia.org/wikipedia/en/b/bb/Apartment_60.jpg",
						"https://www.youtube.com/watch?v=3j9Q6w_3asA")

movies = [zootopia,exmachina,gattaca,madmaxfr,shaunofthedead,apartment]
fresh_tomatoes.open_movies_page(movies)