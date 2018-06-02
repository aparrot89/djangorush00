import sys, requests, json
import omdb
from django.conf import settings

API_KEY = '903c3efb'

MOVIES = [
        'alien',
        'avatar',
        'rocky horror picture show',
        'x-men',
        'avengers',
        'pokemon',
        'batman',
        'shining',
        'Freddy',
        'unbreakable',
        'pacific-rim',
        'robot-monster',
        'dragonball-evolution',
        'vampire-academy',
        'elektra',
        'Mega Shark vs. Giant Octopus',
        'jehrg'
]

class Movie:
    def __init__(self, infos):
        self.title = infos['Title']
        self.img = infos['Poster']
        self.rating = float(infos['imdbRating'])

    def __str__(self):
        ret = ""
        for k, v in self.__dict__.items():
            if not(len(k) >= 4 and k[:2] == "__" and k[-2:] == "__"):
                ret += k + ' : ' + str(v) + '\n'
        return ret

class Game:
    def __init__(self):
        self.movies = []

    def get_movies(self):
        #API_KEY = getattr(settings, 'API_KEY', None)
        omdb.set_default('apikey', API_KEY)

        for movie in MOVIES:
            wp_call = omdb.request(t=movie)
            if wp_call.status_code != 200:
                print("Erreur HTTP, code ", str(wp_call.status_code))
                exit(1)
            infos_json = wp_call.json()
            if infos_json and 'Error' in infos_json.keys():
                print('Error: ', infos_json['Error'])
            else:
                self.movies.append(Movie(infos_json))

    def __str__(self):
        ret = ""
        for movie in self.movies:
            ret += str(movie) + '\n'
        return ret

def main():
    game = Game()
    game.get_movies()
    print(game, end="")


if __name__ == '__main__':
    main()
