import os, pickle
from django.shortcuts import render, HttpResponse
from django.conf import settings
from .game import Game

def init(request):
    return render(request, 'game/base.html')

def worldmap(request):
    pickle_name = get_pickle_name()
    if os.path.exists(pickle_name):
        game = Game.load(pickle_name)
    else:
        game = Game.load_default_settings()
    game.dump()
    return render(request, 'game/worldmap.html', get_worldmap_params(game))

def load(request):
    return HttpResponse("load")

def up(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.mario_y = max(0, game.mario_y - 1)
    game.dump()
    return render(request, 'game/worldmap.html', get_worldmap_params(game))

def down(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.mario_y = min(game.grid_size - 1, game.mario_y + 1)
    game.dump()
    return render(request, 'game/worldmap.html', get_worldmap_params(game))

def left(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.mario_x = max(0, game.mario_x - 1)
    game.dump()
    return render(request, 'game/worldmap.html', get_worldmap_params(game))

def right(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.mario_x = min(game.grid_size - 1, game.mario_x + 1)
    game.dump()
    return render(request, 'game/worldmap.html', get_worldmap_params(game))

def start(request):
    return HttpResponse("start")
def select(request):
    return HttpResponse("select")

def get_pickle_name():
    pickle_name = getattr(settings, "PICKLE_NAME", None)
    if pickle_name is None:
        pickle_name = os.path.join(settings.BASE_DIR, 'infos.pickle')
    return pickle_name

"""
def get_worldmap_params(game):
    return {
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.mario_x = min(game.grid_size - 1, game.mario_x + 1)
    game.dump()
    return render(request, 'game/worldmap.html', get_worldmap_params(game))
"""

def start(request):
    return HttpResponse("start")
def select(request):
    return HttpResponse("select")

def get_pickle_name():
    pickle_name = getattr(settings, "PICKLE_NAME", None)
    if pickle_name is None:
        pickle_name = os.path.join(settings.BASE_DIR, 'infos.pickle')
    return pickle_name

def get_worldmap_params(game):
    return {
        'mario_px_x' : str(game.mario_x * game.nb_pixel),
        'mario_px_y' : str(game.mario_y * game.nb_pixel),
        'nb_pixel' : str(game.nb_pixel),
    }
