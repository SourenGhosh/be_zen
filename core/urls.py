from django.urls import include, path

from core.views import PreviewView

urlpatterns = [
    path('home/', PreviewView.as_view())
]