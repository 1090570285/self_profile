from django.shortcuts import render
from gallery.models import Gallery


def home(request):
    gallerys = Gallery.objects
    return render(request, 'index.html',{'gallerys': gallerys})