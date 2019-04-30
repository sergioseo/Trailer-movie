import webbrowser

# hola

class Head():
    def __init__(self, title, duration, info, poster_image_url):
        """Here we can define the title, duration, info and poster_image"""
        self.title = title
        self.duration = duration
        self.info = info
        self.poster_image_url = poster_image_url


class Movie(Head):
    def __init__(self, title, duration, info, poster_image_url,
                 storyline, release, trailer_youtube_url):
        """Here we will determine the attributes for the movies"""
        Head.__init__(self, title, duration, info, poster_image_url)
        self.storyline = storyline
        self.release = release
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Open the youtube trailers that are selected"""
        webbrowser.open(self.trailer_youtube_url)
