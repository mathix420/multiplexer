import unittest
from multiplexer import multiplexer

'''
These tests are temporary
'''


class TestMultiplexer(unittest.TestCase):

    def test_step(self):
        self.assertEqual(multiplexer._step("dede"), 'f7fda3aabac0ba0eccd\
45cab879068396cdcc2ed8a43a572c33c459e0541ebf2d77294b4dba1c4c30b9dd4d34f2\
dea676127df78e2388b44ed69d79331154d3b71075259a5ed844c31d98b192c3ce215f51\
83127f98bac97af4f97c82538b4d3657a8ffc2078850dcd76d6b1b9704c30be298d98a73\
b37a0e9d2969a9b94e996306fa5bb6ccabe9fddc6b0272652cca2bbfcf691dd6b2a816cf\
d3eb844596cdc139abb81b4f54ca48d768e3f7ddfb82eac96f2228119be7ef90668b739f02980')

        self.assertEqual(multiplexer._step("michel"), 'cf2f7d49a6adb9a7e\
56d9547e9b80c85017cea41910603fc68a24b4a401b79e29eaf10c0ca956fe53e38c593a\
9ae723258971cc0793a24f72ddb9217c2e9c7e7e559aefac6fe1b006d3497abee2649ceb\
71fcceea73fd223782338ab29c08e5b887836b806349d5ace9030c69ca91850b01c46882\
5d02359a5faee7261de415e')

    def test_get_indices(self):
        tests = {
            'cf2f7d49a6adb9a7e': (12, 11),
            '3a24f72ddb9217c2e9c7e7e559aefa': (3, 4),
            'aa0aaa0aa0aa0aa0': (10, 10),
            '0000000000aaa23ef': (10, 10),
            'c0feec0feec0feec0fee': (12, 15),
            'deaddeaddeadead': (13, 10),
        }
        for key, res in tests.items():
            self.assertEqual(multiplexer._get_indices(key), res)

    def test_generate(self):
        book = multiplexer.generate('test-key')
        self.assertGreater(len(book), 1000000)
        book2 = multiplexer.generate('test-key')
        self.assertEqual(book, book2)
        fake_book = multiplexer.generate('fake-key')
        self.assertNotEqual(book, fake_book)
