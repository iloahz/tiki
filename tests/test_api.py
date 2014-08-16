from tiki import api
import unittest


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
            fancy = api.tiki(segment)
            self.assertEqual(min(segment, 8) - 1, fancy.count('('))
            self.assertEqual(min(segment, 8) - 1, fancy.count(')'))


if __name__ == '__main__':
    unittest.main()