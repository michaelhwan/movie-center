import webbrowser

class Movie():
  
  '''This class stores movie related information'''
  def __init__(self, movie_title, poster_image, youtube_trailer):
    self.title = movie_title
    self.poster_image_url = poster_image
    self.trailer_youtube_url = youtube_trailer

  '''Opens a YouTube trailer within the browser without opening a new tab.'''
  def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)
