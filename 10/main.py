#! /usr/bin/env python3

import os
import sys

from time import process_time, sleep

SHOW_ANIMATION = True
N_TICKS = 10905

def main():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        lines = [l.strip() for l in f.readlines()]
        points = [(l[10:16], l[18:24], l[36:38], l[40:42]) for l in lines]
        points = [tuple((int(j) for j in i)) for i in points]

    def pp(points, tick, minX, maxX, minY, maxY):
        os.system('clear')
        dx, dy = (maxX - minX, maxY - minY)
        m = [[' '] * (dx + 1) for _ in range(dy + 1)]
        for (x, y, vx, vy) in points:
            m[y + tick * vy - minY][x + tick * vx - minX] = '*'

        for r in m:
            print(''.join(r))

        print('@t={}'.format(tick))
        sleep(0.600)

    if SHOW_ANIMATION:
        xs, ys, vxs, vys = zip(*points)
        for i in range(N_TICKS + 1):
            X, Y = (zip(xs, vxs), zip(ys, vys))
            dX = [x + i * vx for (x, vx) in X]
            dY = [y + i * vy for (y, vy) in Y]
            minX, maxX, minY, maxY = (min(dX), max(dX), min(dY), max(dY))
            area = (maxX - minX) * (maxY - minY)

            if area < 175 * 175:
                pp(points, i, minX, maxX, minY, maxY)

    p1 = 'AJZNXHKE'
    p2 = N_TICKS

    print('P1: {}'.format(p1))
    print('P2: {}'.format(p2))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
