from django.shortcuts import render, HttpResponse
from django.conf import settings
from .game import Game
import os, pickle

def init(request):
    return render(request, 'game/base.html')

def worldmap(request):
    nb_grid = 10
    size = 450 / nb_grid
    pickle_name = getattr(settings, "PICKLE_NAME", None)
    if pickle_name is None:
        pickle_name = os.path.join(settings.BASE_DIR, 'infos.pickle')
    game = Game()
    if os.path.exists(pickle_name):
        with open(pickle_name, 'rb') as fd:
            game_attr = pickle.load(fd)
            game.load(game_attr)
    else:
        game.load_default_settings()

    game.dump()
    return render(request, 'game/worldmap.html', {'size': '45'})

def load(request):
    return HttpResponse("load")

def up(request):
    return HttpResponse("up")
def down(request):
    return HttpResponse("down")
def left(request):
    return HttpResponse("left")
def right(request):
    return HttpResponse("right")

def start(request):
    return HttpResponse("start")
def select(request):
    return HttpResponse("select")
