from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from django.core.files.storage import FileSystemStorage

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
        print(video_name)
        form = MediaConverterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        messages.success(request, 'Form submission successful')
        return render(
            request,
            'core/index.html',
        )