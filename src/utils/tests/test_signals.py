from django.core.files.uploadedfile import SimpleUploadedFile

from utils.models import Image
from utils.tests import CustomTestCase


class DeleteImageFileSignalTest(CustomTestCase):
    def setUp(self) -> None:
        self.image = SimpleUploadedFile('test_image.png', b'', content_type='image/png')

    def test_signal_deletes_image_file_after_deleting_image(self):
        image = Image.objects.create(name='name', image=self.image)
        image.delete()
