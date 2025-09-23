from enum import Flag


class OrderStatus(Flag):
    ORDER_PLACED = 1
    PAYMENT_RECEIVED = 2
    SHIPPING_COMPLETE = 4

class MovieGenres(Flag):
    ACTION = 1
    COMEDY = 2
    DRAMA = 4
    FANTASY = 8
    HORROR = 16

class Movie:
    def __init__(self, name, genres: MovieGenres):
        self.name = name
        self.genres = genres

    def in_genre(self, genre: MovieGenres):
        return genre in self.genres
    def __str__(self):
        return self.name