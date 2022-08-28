from django.urls import include, path

from core.views import PreviewView, SearchView


urlpatterns = [
    path('home/', PreviewView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search')
]