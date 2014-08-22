from tiki import api
import unittest
import string
import random


class TestApi(unittest.TestCase):
    def test_default_generate(self):
        for i in range(32):
            fancy = api.tiki()
            print(fancy)
            self.assertNotEqual(fancy, None)
            self.assertNotEqual(fancy, '')

    def test_given_segment(self):
        for i in range(32):
            segment = int(i / 3) + 1
            fancy = api.tiki(segment=segment)
            self.assertEqual(min(segment, 8) - 1, fancy.count('('))
            self.assertEqual(min(segment, 8) - 1, fancy.count(')'))

    def test_given_prefix(self):
        for i in range(32):
            prefix = ''.join([string.ascii_lowercase[random.randint(0, 25)] for j in range(i + 2)])
            fancy = api.tiki(prefix=prefix)
            fancy = ''.join(j for j in fancy if j in string.ascii_lowercase)
            self.assertTrue(fancy.startswith(prefix))


if __name__ == '__main__':
    unittest.main()