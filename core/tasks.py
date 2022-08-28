import string
import os
import shutil
import subprocess
from pathlib import Path
from django.conf import settings

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task
from core.models import MediaConverter

@shared_task
def make_subtitle_from_videos(saved_path, file_id):
    print("inside celery tasks...........................")
    base_dir = settings.BASE_DIR
    file_dir = Path(f"{base_dir}/{saved_path}")

    print(file_dir.parent)
    command = f'ccextractor {file_dir}'
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(error)
    with open(f'{file_dir.parent}/{file_id}.srt', "r") as fe:
        subs=fe.read()
        instance_obj = MediaConverter.objects.get(id=file_id)
        instance_obj.subtitle =subs
        instance_obj.save()

    file = file_dir.parent.parent
    shutil.rmtree(str(file))