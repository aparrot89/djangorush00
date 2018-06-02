from django.shortcuts import render, HttpResponse

# Create your views here

def init(request):
    return render(request, 'game/django.html')

def coucou(request):
    #return HttpResponse("coucou")
    print('coucou')
    return render(request, 'game/coucou.html')
