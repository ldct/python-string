#!/usr/bin/env python3

import timeit

NUMBER = 1

def join(n):
    l = []
    for i in range(n):
        l += ['a']
    return ''.join(l)

def time_for_join(n):
    return timeit.timeit(lambda: join(n), number=NUMBER)

def concat(n):
    ret = ''
    for i in range(n):
        ret = ret + 'a'
    return ret

def time_for_concat(n):
    return timeit.timeit(lambda: concat(n), number=NUMBER)


def concat_left(n):
    ret = ''
    for i in range(n):
        ret = 'a' + ret
    return ret

def time_for_concat_left(n):
    return timeit.timeit(lambda: concat_left(n), number=NUMBER)

for i in range(1, 1000000, 1000):
    baseline = time_for_join(i)

    a = time_for_concat(i) / baseline
    b = time_for_concat_left(i) / baseline

    print(f"{a}\t{b}")