import io
import unittest
from unittest import mock

from imgflip.cli import main

from .utils import mocked_get_memes


class TestCli(unittest.TestCase):

    @mock.patch('sys.stdout', new_callable=io.StringIO)
    @mock.patch('requests.get', side_effect=mocked_get_memes)
    def test_main(self, mock_get, mock_stdout):
        main(['memes'])
        self.assertEqual(len(mock_stdout.getvalue().split('\n')), 101)


if __name__ == '__main__':
    unittest.main()
