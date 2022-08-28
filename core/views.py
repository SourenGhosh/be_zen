from django.shortcuts import render
from django.http import HttpResponse

from django.views import View

from core.models import MediaConverter
from core.forms import MediaConverterForm

class PreviewView(View):
    def get(self, request, *args, **kwargs):
        form = MediaConverterForm()
        return render(
            request,
            'core/index.html',
            {'form': form}
        )

    def post(self, request, *args, **kwargs):
        video_name = request.POST.get('name')
        return render(
            request,
            'core/index.html'
        )