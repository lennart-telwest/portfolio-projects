import webbrowser

class Movie():
    """This class provides a way to store movie related information"""
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """Initialize an instance of Movie with the movie's title, storyline, poster_image and trailer"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
