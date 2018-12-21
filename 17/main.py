#! /usr/bin/env python3

import os
import sys

from collections import defaultdict
from time import process_time

sys.setrecursionlimit(2700)

def main():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        lines = [l.strip() for l in f.readlines()]

    p1 = p2 = None
    clay = defaultdict(bool)
    for line in lines:
        astr, bstr = line.split(', ')
        is_vert = astr[0] == 'x'
        a = int(astr[2:])
        minb, maxb = map(int, bstr[2:].split('..'))
        for b in range(minb, maxb + 1):
            clay[a + b * 1j if is_vert else b + a * 1j] = True

    ys = [p.imag for p in clay]
    ymin, ymax = min(ys), max(ys)
    settled = set()
    flowing = set()

    def fill(p, d=1j):
        flowing.add(p)
        left, below, right = p-1, p+1j, p+1

        if not clay[below]:
            if below not in flowing and 1 <= below.imag <= ymax:
                fill(below)

            if below not in settled:
                return False

        left_filled =  clay[left]  or left  not in flowing and fill(left, -1)
        right_filled = clay[right] or right not in flowing and fill(right, 1)

        if d == 1j and left_filled and right_filled:
            settled.add(p)

            while left in flowing:
                settled.add(left)
                left -= 1

            while right in flowing:
                settled.add(right)
                right += 1

        return (d == -1 and (left_filled or clay[left]) or
                d ==  1 and (right_filled or clay[right]))

    fill(500)

    p1 = len([p for p in flowing | settled if ymin <= p.imag <= ymax])
    p2 = len([p for p in settled if ymin <= p.imag <= ymax])

    print('P1: {}'.format(p1))
    print('P2: {}'.format(p2))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
