import os, pickle
from django.shortcuts import render, HttpResponse
from django.conf import settings
from .game import Game

def init(request):
    pickle_name = get_pickle_name()
    if os.path.exists(pickle_name):
        os.remove(pickle_name)
    return render(request, 'game/base.html')

def options(request):
    return render(request, 'game/options.html')

def moviedex(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    list_pokemon = [m for m in game.moviedex.values()]
    name = list_pokemon[game.slot].title if len(list_pokemon) > 0 else ""
    return render(request, 'game/moviedex.html', {"moviedex": list_pokemon, 'pos': game.slot + 1, 'name': str(name)})

def moviedex_up(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.slot = max(game.slot - 1, 0)
    game.dump()
    list_pokemon = [m for m in game.moviedex.values()]
    name = list_pokemon[game.slot].title if len(list_pokemon) > 0 else ""
    return render(request, 'game/moviedex.html', {"moviedex": list_pokemon, 'pos': game.slot + 1, 'name': str(name)})


def moviedex_down(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.slot = min(game.slot + 1, len(game.moviemons) - 1)
    game.dump()
    list_pokemon = [m for m in game.moviedex.values()]
    name = list_pokemon[game.slot].title if len(list_pokemon) > 0 else ""
    return render(request, 'game/moviedex.html', {"moviedex": list_pokemon, 'pos': game.slot + 1, 'name': str(name)})

def details(request, moviemon):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    return render(request, 'game/details.html', {"moviemon": game.moviemons[moviemon]})

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

    game.slot = min(game.slot + 1, )

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

def save(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    print(moviemon)
    game.dump()
    return render(request, 'game/save.html', get_save_params(game.slot))

def save_A(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.dump(game.slot)
    return render(request, 'game/save.html', get_save_params(game.slot))

def save_B(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.slot = 0
    game.dump()
    return render(request, 'game/options.html')

def save_up(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.slot = max(game.slot - 1, 0)
    game.dump()
    return render(request, 'game/save.html', get_save_params(game.slot))

def save_down(request):
    pickle_name = get_pickle_name()
    game = Game.load(pickle_name)
    game.slot = min(game.slot + 1, 2)
    game.dump()
    return render(request, 'game/save.html', get_save_params(game.slot))

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

def get_save_params(slot):
    slots_name = ['a', 'b', 'c']
    slots = {}
    for slot_name in slots_name:
        slots[slot_name] = {}
    slots['a']
    save_dir = getattr(settings, 'SAVE_DIR', os.path.join(settings.BASE_DIR, 'saved_game'))
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    files = [os.path.join(save_dir, elem) for elem in os.listdir(save_dir) if os.path.isfile(os.path.join(save_dir, elem))]
    for elem in files:
        for slot_name in slots_name:
            if 'slot' + slot_name in elem:
                game = Game.load(elem)
                slots[slot_name]['dex_number'] = len(game.moviedex)
                slots[slot_name]['mons_number'] = slots['a']['dex_number'] + len(game.moviemons)
    slots['pos'] = slot
    return slots
