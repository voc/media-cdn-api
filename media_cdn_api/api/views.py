import json
from django.http import HttpResponse
from django.shortcuts import render
from media_cdn_api.api.models import Server
from media_cdn_api.api.hexhash import Hexhash
from media_cdn_api.api.mirror_info import MirrorInfo

def torrents(request):
    data = Hexhash().all()
    return HttpResponse("\n".join(data), content_type='application/text')

def mirrors(request):
    mirrors = Server.objects.filter(enabled=True)
    mi = MirrorInfo()
    data = [mi.dict(mirror) for mirror in mirrors]
    return HttpResponse(json.dumps(data), content_type='application/json')


