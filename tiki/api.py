from .utils import rand
from .trie import words, trie


DEFAULT_SEGMENT_PRB = [50,    500,    400,    200,    30,     20,     15,     10]
CURRENT_SEGMENT_PRB = DEFAULT_SEGMENT_PRB
CURRENT_SEGMENT_LEN = len(CURRENT_SEGMENT_PRB)


def set_segment_prb(prb):
    global CURRENT_SEGMENT_PRB, CURRENT_SEGMENT_LEN
    CURRENT_SEGMENT_PRB = prb
    CURRENT_SEGMENT_LEN = len(CURRENT_SEGMENT_PRB)


def tiki(segment=0, prefix=''):
    if segment <= 0:
        segment = rand([i + 1 for i in range(CURRENT_SEGMENT_LEN)],
                       CURRENT_SEGMENT_PRB)
    segment = min(segment, 8)
    result = prefix
    if result == '':
        result = rand(words, [i + 1 for i in range(len(words))])
    if result not in words:
        trie.insert(result)
    last_word = result[1:]
    for i in range(1, segment):
        overlap_len = rand([j + 1 for j in range(len(last_word))],
                           [(j + 1)**5 for j in range(len(last_word))])
        for j in range(overlap_len, 0, -1):
            overlap = last_word[-j:]
            next_opt = trie.find(overlap)
            if len(next_opt):
                next_opt.sort(key=len)
                next_word = rand(next_opt, [k + 1 for k in range(len(next_opt))])
                result = result[:-j] + '(' + overlap + ')' + next_word
                last_word = next_word
                break
    return result

if __name__ == '__main__':
    for i in range(32):
        print(tiki())
