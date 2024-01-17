import os
from pathlib import Path

from django.conf import settings


def get_upload_filename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'images/{instance.uuid}.{ext}'
    path = Path(settings.MEDIA_ROOT, filename)
    if path.exists():
        os.remove(path)
    return filename
