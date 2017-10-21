"""A constructor module for various media"""
import webbrowser


class Movie:
    '''A constructor class for various movies'''
    def __init__(self, title, description, run_time, genre, youtube_url, img_url):
        self.title = title
        self.description = description
        self.run_time = run_time
        self.genre = genre
        self.youtube_url = youtube_url
        self.img_url = img_url

    def show_trailer(self):
        webbrowser.open(self.youtube_url, new=2)
