##########################################
# Project 0: Movie Website
# Date Started: 10/01/2017
# Date Completed: 10/02/2017
# Submitted by: Wonhyeong Seo
##########################################

######################################## Media File ####################################################
# Description: This file creates the class Movie to allow for instances of this class to be used in the
#              entertainment.py file. This definition of the class Movie was obtained through the course
########################################################################################################
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
