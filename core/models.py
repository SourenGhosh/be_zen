import pytz
import uuid
from django.db import models


class BeZenBase(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract=True


def video_attachment_file(instance, filename):
    return f"files/{instance.name}/video/{instance.id}"

def subs_attachment_path(instance, filename):
    return f"files/{instance.name}/subs/{instance.id}_{filename}"

class MediaConverter(BeZenBase):
    name = models.CharField(max_length=70, default = 'test')
    attachment = models.FileField(upload_to = video_attachment_file, null=True, blank=True)
    subtitle = models.TextField(null=True, blank=True)

    @property
    def subs_attachment_path(self):
        return f"files/{self.name}/video"


        
    def __str__(self):
        return self.name

    
