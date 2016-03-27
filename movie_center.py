import fresh_tomatoes
import media

# Some of my favorite movies right now. More will be added soon!

inception = media.Movie("Inception",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/7/7f/Inception_ver3.jpg/220px-Inception_ver3.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0")

avatar = media.Movie("Avatar",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

ex_machina = media.Movie("Ex Machina",
                         "https://upload.wikimedia.org/wikipedia/en/b/ba/Ex-machina-uk-poster.jpg",
                         "https://www.youtube.com/watch?v=EoQuVnKhxaM")

star_wars = media.Movie("Star Wars",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg/220px-Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
                        "https://www.youtube.com/watch?v=sGbxmsDFVnE")

# An array of all the movies currently in the Movie Center.
movies = [inception, avatar, ex_machina, star_wars]

# Uses a function in the fresh_tomatoes.py file to output the movie_title, movie_storyline, poster_image, and youtube_trailer in the browser.
fresh_tomatoes.open_movies_page(movies)
