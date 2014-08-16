from random import randint


def rand(opt, prb):
    s = [0]
    for idx, val in enumerate(prb):
        s.append(s[idx] + val)
    choose = randint(1, s[-1])
    for idx, val in enumerate(opt):
        if choose <= s[idx + 1]:
            return val
    return None