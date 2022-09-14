# TODO: Implement Routings Here
from django.urls import path
from katalog.views import show_catalogitem

app_name = 'Katalog'

urlpatterns = [
    path('', show_catalogitem, name='show_catalogitem'),
]