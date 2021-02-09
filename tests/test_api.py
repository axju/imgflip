import os
import json
import unittest
from unittest import mock

from imgflip.api import Client
from imgflip.utils import ResponseImage

from .utils import mocked_get_memes, mocked_caption_image


class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client('username', 'password', 'http://localhost/')

    @mock.patch('requests.get', side_effect=mocked_get_memes)
    def test_get_memes(self, mock_get):
        memes = self.client.get_memes()
        self.assertIsInstance(memes, list)

    @mock.patch('requests.post', side_effect=mocked_caption_image)
    def test_caption_image(self, mock_get):
        image = self.client.caption_image(identifier=0, text0='test', text1='test')
        self.assertIsInstance(image, ResponseImage)


if __name__ == '__main__':
    unittest.main()
