import os
from trie import Trie
from random import randint
CUR_DIR = os.path.dirname(os.path.realpath(__file__))


def rand(opt, prb):
    s = [0]
    for idx, val in enumerate(prb):
        s.append(s[idx] + val)
    choose = randint(1, s[-1])
    for idx, val in enumerate(opt):
        if choose <= s[idx + 1]:
            return val
    return None


src = os.path.join(CUR_DIR, 'dict.txt')
words = [word.rstrip('\n') for word in open(src)]
words.sort(key=len)
root = Trie()
for word in words:
    root.insert(word)


def tiki(segment=0):
    if segment <= 0:
        segment = rand([1,     2,      3,      4,      5,      6,      7,      8],
                       [100,   1000,   200,    100,    30,     20,     15,     10])
    segment = min(segment, 8)
    result = rand(words, [i for i in range(1, len(words) + 1)])
    last_word = result[1:]
    for i in range(1, segment):
        overlap_len = rand([j + 1 for j in range(len(last_word))],
                           [j * j * j for j in range(1, len(last_word) + 1)])
        for j in range(overlap_len, 0, -1):
            overlap = last_word[-j:]
            next_opt = root.find(overlap)
            if len(next_opt):
                next_opt.sort(key=len)
                next_word = rand(next_opt, [k for k in range(1, len(next_opt) + 1)])
                result = result[:-j] + '(' + overlap + ')' + next_word
                last_word = next_word
                break
    return result

if __name__ == '__main__':
    for i in range(32):
        print(tiki())