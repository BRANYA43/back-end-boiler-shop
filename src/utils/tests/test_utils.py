from unittest.mock import Mock, patch

from django.conf import settings

from utils.models import Image
from utils.tests import CustomTestCase
from utils.utils import get_upload_filename


class GetUploadFilenameTest(CustomTestCase):
    def setUp(self) -> None:
        self.instance = Image()
        self.filename = 'some_image.png'

    def test_get_upload_path_method_returns_correct_filename(self):
        filename = get_upload_filename(self.instance, self.filename)
        correct_path = f'images/{self.instance.uuid}.png'

        self.assertEqual(filename, correct_path)

    @patch('pathlib.Path.exists', return_value=True)
    @patch('os.remove')
    def test_get_upload_path_method_removes_existing_file_by_path(self, mock_remove: Mock, mock_exists: Mock):
        filename = get_upload_filename(self.instance, self.filename)

        mock_exists.assert_called_once_with()
        mock_remove.assert_called_once_with(settings.MEDIA_ROOT / filename)
