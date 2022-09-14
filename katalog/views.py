from multiprocessing import context
from django.shortcuts import render
from katalog.models import CatalogItem
# TODO: Create your views here.

def show_catalogitem(request):
    data_catalog_item = CatalogItem.objects.all()
    context = {
        'list_catalog_item': data_catalog_item,
        'nama': 'Arditio Reihansyah Putra Pradana',
        'npm' : '2106751972'
    }
    return render(request,"katalog.html",context)
