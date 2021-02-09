import logging
from imgflip.utils import ResponseImage, get_memes, caption_image


class Client:
    """docstring for Client."""

    def __init__(self, username='', password='', root_url='https://api.imgflip.com/'):
        super().__init__()
        self.logger = logging.getLogger('{}.{}'.format(__name__, self.__class__.__name__))
        self.logger.debug('create')
        self.username = username
        self.password = password
        self.urls = {
            'get_memes': root_url + 'get_memes',
            'caption_image': root_url + 'caption_image',
        }
        self.memes = []

    def get_memes(self, update=False):
        if len(self.memes) == 0 or update:
            self.memes = get_memes(url=self.urls['get_memes'])
        return self.memes

    def caption_image(self, identifier=None, index=-1, **kwargs):
        if identifier is None:
            if len(self.memes) == 0:
                self.get_memes()
            self.logger.debug('%i %i %s', len(self.memes), index, index in range(len(self.memes)))
            if index in range(len(self.memes)):
                identifier = self.memes[index].get('id')

        if identifier is None:
            print('Error')

        text0 = kwargs.get('text0')
        text1 = kwargs.get('text1')
        data = caption_image(identifier, self.username, self.password, text0, text1, url=self.urls['caption_image'])
        return ResponseImage(data['data']['url'])
