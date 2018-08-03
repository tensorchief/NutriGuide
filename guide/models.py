from django.db import models


# Create your models here.
class TitleCard(object):

    def __init__(self, title, description, colour, icon):
        self.icon = icon
        self.colour = colour
        self.title = title
        self.description = description
