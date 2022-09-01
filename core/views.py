from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views import View
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from core.models import MediaConverter
from core.forms import MediaConverterForm


from core.tasks import make_subtitle_from_videos
from core.utils import search_subs
class PreviewView(View):
    def get(self, request, *args, **kwargs):
        form = MediaConverterForm()
        qs  = MediaConverter.objects.all()
        return render(
            request,
            'core/index.html',
            {'form': form, 'qs': qs}
        )

    def post(self, request, *args, **kwargs):
        video_name = request.POST.get('name')
        print(video_name)
        form = MediaConverterForm(request.POST, request.FILES)
        if form.is_valid():
            generated_instance = form.save()
        #make_subtitle_from_videos.delay(generated_instance.attachment.url, generated_instance.id)
        make_subtitle_from_videos(generated_instance.attachment.url, generated_instance.id)
        messages.success(request, 'Form submission successful')
        return redirect(
            reverse('home')
        )



class SearchView(View):
    def post(self, request, *args, **kwargs):
        keyword = request.POST.get('search')
        id = kwargs.get('id')
        print("................", id)
        timeframes = search_subs(keyword, id)
        return render(
            request,
            'core/search_result.html',
            {'results': timeframes}
        )