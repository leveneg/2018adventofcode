#! /usr/bin/env python3

import os
import sys

from time import process_time

INPUT = 380621
DIGITS = [int(i) for i in str(INPUT)]

def main():
    p1 = p2 = None

    elves = [0, 1]
    scores = [3, 7]

    while not (p2 and p1):
        _scores = [scores[i] for i in elves]
        s = sum(scores[i] for i in elves)
        scores += [d for d in [s // 10 % 10 or None, s % 10] if d != None]
        elves = [(i + s + 1) % len(scores) for i, s in zip(elves, _scores)]

        if not p1 and len(scores) >= INPUT + 10:
            p1 = ''.join(str(i) for i in scores[-10:])

        if not p2:
            tail = [scores[-len(DIGITS):], scores[-len(DIGITS)-1:-1]]
            if DIGITS in tail:
                p2 = len(scores) - len(DIGITS) - tail.index(DIGITS)

    print('P1: {}'.format(p1))
    print('P2: {}'.format(p2))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
