from django.shortcuts import render
from django.http import HttpResponse

from django.views import View



class PreviewView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'core/index.html'
        )

    def post(self, request, *args, **kwargs):
        video_name = request.POST.get('name')
        return render(
            request,
            'core/index.html'
        )