from django.shortcuts import render
#from media_cdn_api.api.models import Hexhash

def torrents(request):
    hashes = Hexhash.objects.raw('SELECT f.path, h.btihhex FROM hexhash h JOIN filearr f ON f.id = h.file_id}')
    return render(request, 'torrents/index.html', {'torrents': hashes})

def mirrors(request):
    mirrors = Server.objects.filter(enabled=True)
    return render(request, 'mirrors/index.html', {'mirrors': mirrors})

