#! /usr/bin/env python3

import os
import sys

from time import process_time

def main():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        inp = [int(n) for n in f.read().strip().split(' ')]

    def s(rem):
        nc, nm, rest = rem[0], rem[1], rem[2:]
        vals = []
        res = 0

        for _ in range(nc):
            t, rest, val =  s(rest)
            res += t
            vals.append(val)

        res += sum(rest[:nm])

        if nc:
            val = sum(vals[c-1] for c in rest[:nm] if c > 0 and c <= len(vals))
        else:
            val = sum(rest[:nm])


        return (
            res,
            rest[nm:],
            val
        )

    total, _, val = s(inp)

    p1 = total
    p2 = val

    print('P1: {}'.format(p1))
    print('P2: {}'.format(p2))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
