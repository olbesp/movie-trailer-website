import webbrowser


class Movie():
    """This class provides a way to store movie related information"""
    def __init__(self, movie_title, poster_image, movie_trailer):
        # This function initializes next methods with class Movie
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        # This function takes trailer link and opens it in a browser
        webbrowser.open(self.trailer_youtube_url)
