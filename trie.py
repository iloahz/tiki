class Trie():
    def __init__(self):
        self.son = [None] * 26
        self.sink = False

    def insert(self, s, cur=0):
        if cur >= len(s):
            self.sink = True
            return
        idx = ord(s[cur]) - 97
        if self.son[idx] is None:
            self.son[idx] = Trie()
        self.son[idx].insert(s, cur + 1)

    def dfs(self, cur, result):
        if self.sink and len(cur) > 0:
            result.append(cur)
        for i in range(26):
            if self.son[i]:
                self.son[i].dfs(cur + chr(i + 97), result)

    def find(self, s, cur=0):
        if cur >= len(s):
            result = []
            self.dfs('', result)
            return result
        idx = ord(s[cur]) - 97
        if self.son[idx] is None:
            return []
        return self.son[idx].find(s, cur + 1)