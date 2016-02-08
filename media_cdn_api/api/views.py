from django.shortcuts import render
#from media_cdn_api.api.models import Hexhash

def torrents(request):
    # TODO bypass model layer
    hashes = Hexhash.new.all()
    return render(request, 'torrents/index.html', {'torrents': hashes})

def mirrors(request):
    mirrors = Server.objects.filter(enabled=True)
    return render(request, 'mirrors/index.html', {'mirrors': mirrors})


