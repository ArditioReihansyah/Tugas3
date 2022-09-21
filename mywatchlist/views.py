from django.shortcuts import render
from mywatchlist.models import watchlist
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    data_mywatchlist = watchlist.objects.all()
    context = {
        'list_mywatchlist': data_mywatchlist,
        'nama': 'Arditio Reihansyah Putra Pradana',
        'npm' : '2106751972'
    }
    return render(request,"mywatchlist.html",context)

def show_xml(request):
    data = watchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = watchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")