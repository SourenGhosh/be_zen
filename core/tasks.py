import string
import re
import os
import shutil
import subprocess
import boto3

from pathlib import Path
from django.conf import settings

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from celery import shared_task
from core.models import MediaConverter
from configparser import RawConfigParser



def upload_video(file_dir, file_id):
    instance_obj = MediaConverter.objects.get(id=file_id)
    filename = instance_obj.name

    config = RawConfigParser()



    config.read(os.path.join(settings.BASE_DIR, f'{os.environ.get("ENV")}.ini'))

    client = boto3.client(
        's3',
        aws_access_key_id=config.get('AWS_CRED', 'access_key_id'),
        aws_secret_access_key=config.get('AWS_CRED', 'secret_access_key'),
    )
    print("................", file_dir)
    with open(file_dir, 'rb') as f:
        client.upload_fileobj(f, config.get('AWS_CRED', 'bucket_name'), filename)

#@shared_task
def make_subtitle_from_videos(saved_path, file_id):
    print("inside celery tasks...........................")
    base_dir = settings.BASE_DIR
    file_dir = Path(f"{base_dir}/{saved_path}")
    print(file_dir.parent)
    upload_video(file_dir, file_id)
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


@shared_task
def search_subs(keyword, query_id):
    serach_obj = MediaConverter.objects.get(id=id)
    subs = search_obj.subtitle
    segment_list = list()
    alloc_seg = list()
    for line in subs.split('\n'):
        temp_seg = re.findall(r"\d{1}\:\d{2}\:\d{2}\,\d{3}", line)
        if temp_seg:
            alloc_seg = temp_seg
        if x in " ".join(line.split()):
            segment_list.append(alloc_seg)
    return segment_list

