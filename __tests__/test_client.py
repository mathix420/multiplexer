import unittest
from string import printable
from binascii import hexlify
from random import choice, randint
from multiplexer import Plex, generate

'''
These tests are temporary
'''


def rnd_string(size):
    return ''.join(choice(printable) for i in range(size))


class TestClient(unittest.TestCase):

    def test_security(self):
        self.assertRaises(Exception, Plex, hexlify(
            printable.encode()).decode())

    def test_good_book(self):
        book = generate('michel')
        client = Plex(book)
        self.assertTrue(client.len)

    def test_encoding_decoding(self):
        book = generate(rnd_string(randint(5, 128)))
        client = Plex(book)
        text = rnd_string(randint(200, 1000))
        res = client.encode(text)
        self.assertEqual(client.decode(res), text)
