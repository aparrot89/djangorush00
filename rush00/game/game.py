import sys, requests, json
import omdb
from django.conf import settings
import pickle

class Moviemon:
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
        self.moviemons = {}
        self.moviedex = {}
        self.mario_x = 0
        self.mario_y = 0
        self.nb_movieballs = 50

    def omdb_request(self):
        API_KEY = getattr(settings, 'API_KEY', None)
        if API_KEY is None:
            print("Error: no API_KEY in settings.py")
            exit(1)
        moviemons = getattr(settings, 'MOVIEMONS', None)
        if moviemons is None:
            print("Error: no moviemons in settings.py")
            exit(1)
        omdb.set_default('apikey', API_KEY)
        for movie in moviemons:
            wp_call = omdb.request(t=movie)
            if wp_call.status_code != 200:
                print("Erreur HTTP, code ", str(wp_call.status_code))
                exit(1)
            infos_json = wp_call.json()
            if infos_json and 'Error' in infos_json.keys():
                print('Error: ', infos_json['Error'])
            else:
                self.moviemons[infos_json['Title']] = Moviemon(infos_json)

    def load(self, game_dict):
        self.moviemons = game_dict['moviemons']
        self.moviedex = game_dict['moviedex']
        self.mario_x = game_dict['mario_x']
        self.mario_y = game_dict['mario_y']
        self.nb_movieballs = game_dict['nb_movieballs']

    def load_default_settings(self):
        self.omdb_request()
        self.moviedex = {}
        self.mario_x = getattr(settings, 'MARIO_X', None)
        self.mario_y = getattr(settings, 'MARIO_Y', None)
        self.nb_movieballs = getattr(settings, 'NB_MOVIEBALLS', None)
        if self.mario_x is None or self.mario_y is None or self.nb_movieballs is None:
            print("Error: MARIO_X or MARIO_Y or NB_MOVIEBALLS is not set in settings.py")
            exit(1)

    def dump(self):
        pickle_name = getattr(settings, "PICKLE_NAME", None)
        if pickle_name is None:
            pickle_name = os.path.join(settings.BASE_DIR, 'infos.pickle')
        with open(pickle_name, 'wb') as fd:
            tmp = self.__dict__
            to_dump = {}
            to_dump['moviemons'] = tmp['moviemons']
            to_dump['moviedex'] = tmp['moviedex']
            to_dump['mario_x'] = tmp['mario_x']
            to_dump['mario_y'] = tmp['mario_y']
            to_dump['nb_movieballs'] = tmp['nb_movieballs']
            pickle.dump(to_dump, fd)

    def __str__(self):
        ret = ""
        for title, movie in self.moviemons.items():
            ret += str(movie) + '\n'
        return ret

def main():
    game = Game()
    game.omdb_request()
    print(game, end="")


if __name__ == '__main__':
    main()
