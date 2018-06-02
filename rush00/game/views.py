from django.shortcuts import render, HttpResponse

def init(request):
    return render(request, 'game/base.html')

def worldmap(request):
    return render(request, 'game/worldmap.html')

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
