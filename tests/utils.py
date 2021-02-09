import os
import json


class MockResponse:
    def __init__(self, json_data_file, status_code):
        with open(json_data_file) as json_file:
            self.json_data = json.load(json_file)
        self.status_code = status_code

    def json(self):
        return self.json_data


def mocked_get_memes(*args, **kwargs):
    json_data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'utils', 'get_memes.json')
    return MockResponse(json_data_file, 200)


def mocked_caption_image(*args, **kwargs):
    json_data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'utils', 'caption_image.json')
    return MockResponse(json_data_file, 200)
