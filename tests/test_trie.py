import unittest
from tiki.trie import Trie
from tiki.trie import trie
import string
import random


def random_string(size=8):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(size))


class TestTrie(unittest.TestCase):
    def test_default_dict(self):
        existing_words = ['indeed', 'love', 'world', 'yeah', 'romantic']
        for word in existing_words:
            self.assertTrue(trie.exist(word))
        non_existing_words = ['idont', 'geet', 'hurtings']
        for word in non_existing_words:
            self.assertFalse(trie.exist(word))

    def test_basic_insert_and_find(self):
        words = [random_string(i // 2 + 1) for i in range(32)]
        words.sort()
        t = Trie()
        for word in words:
            t.insert(word)
        for word in words:
            self.assertTrue(t.exist(word))
        result = t.find('')
        result.sort()
        self.assertListEqual(words, result)
