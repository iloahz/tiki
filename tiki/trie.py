import os


class Trie():
    def __init__(self):
        self.son = [None] * 26
        self.sink = False

    def insert(self, s):
        cur_node = self
        for i in s:
            idx = ord(i) - 97
            if cur_node.son[idx] is None:
                cur_node.son[idx] = Trie()
            cur_node = cur_node.son[idx]
        cur_node.sink = True

    def dfs(self, cur, result):
        if self.sink and len(cur) > 0:
            result.append(cur)
        for i in range(26):
            if self.son[i]:
                self.son[i].dfs(cur + chr(i + 97), result)

    def find(self, s):
        cur_node = self
        for i in s:
            idx = ord(i) - 97
            if cur_node.son[idx] is None:
                return []
            cur_node = cur_node.son[idx]
        result = []
        cur_node.dfs('', result)
        return result

    def exist(self, s):
        cur_node = self
        for i in s:
            idx = ord(i) - 97
            if cur_node.son[idx] is None:
                return False
            cur_node = cur_node.son[idx]
        return cur_node.sink


CUR_DIR = os.path.dirname(os.path.realpath(__file__))
src = os.path.join(CUR_DIR, 'dict.txt')
words = [word.rstrip('\n') for word in open(src)]
words.sort(key=len)
trie = Trie()
for word in words:
    trie.insert(word)