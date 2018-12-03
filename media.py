import webbrowser


class Head():
    def __init__(self, title, duration, info, poster_image_url):
        """Aqui podemos definir o title, duration, info e poster_image"""
        self.title = title
        self.duration = duration
        self.info = info
        self.poster_image_url = poster_image_url


class Movie(Head):
    def __init__(self, title, duration, info, poster_image_url,
                 storyline, release, trailer_youtube_url):
        """Aqui iremos determinar os atributos para os filmes"""
        Head.__init__(self, title, duration, info, poster_image_url)
        self.storyline = storyline
        self.release = release
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """Serão abertos os trailers no youtube que são selecionados"""
        webbrowser.open(self.trailer_youtube_url)
