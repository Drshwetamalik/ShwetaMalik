from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required



from django.views.generic import (TemplateView)



class AboutView(TemplateView):
    template_name = 'about.html'

class baseView(TemplateView):
    template_name = 'base.html'

class FavouritesView(TemplateView):
    template_name = 'favourites.html'

