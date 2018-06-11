import webbrowser

class Movie():
    '''
    Defines a movie class.
    '''
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title      = title
        self.storyline  = storyline
        self.poster_image_url     = poster_image_url
        self.trailer_youtube_url    = trailer_youtube_url

    def showTrailer(self):
        webbrowser.open(self.trailer)

class Parent():
    def __init__(self, last_name, eye_color):
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, toys):
        Parent.__init__(self, last_name, eye_color)
        self.toys = toys

