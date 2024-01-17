from utils.tests import CustomTestCase
from utils.tests.creators import create_test_image


class DeleteImageFileSignalTest(CustomTestCase):
    def test_signal_deletes_image_file_after_deleting_image(self):
        image = create_test_image()
        image.delete()
