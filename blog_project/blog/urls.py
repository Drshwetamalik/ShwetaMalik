from django.conf.urls import url
from . import views
from django.urls import path


urlpatterns = [
    
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'',views.baseView.as_view(),name='base'),
    url(r'^favourites/$',views.FavouritesView.as_view(),name='favourites'),
   
]