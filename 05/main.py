#! /usr/bin/env python3

import os
import sys

from string import ascii_uppercase
from time import process_time

def compress(s):
    res = []
    for c in s:
        if res and abs(ord(c) - ord(res[-1])) == 2 ** 5:
            res.pop()
        else:
            res.append(c)

    return len(res)

def main():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        s = f.read().strip()

    p1 = compress(s)
    p2 = len(s)

    for c in ascii_uppercase:
        d = [l for l in s if l != c.lower() and l != c]
        p2 = min(p2, compress(d))

    print('P1: {}'.format(p1))
    print('P2: {}'.format(p2))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
