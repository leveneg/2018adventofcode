#! /usr/bin/env python3

import os
import sys

from collections import defaultdict, namedtuple
from heapq import heappush, heappop
from math import inf
from time import process_time

SHOW_ANIMATION = True

def main():
    def simulate(units, elfap=3):
        def ns(p):
            return [p-1j, p-1, p+1, p+1j]

        def np(unit):
            foes = [u for u in units if u.type != unit.type and u.hp > 0]
            targets = [n for u in foes for n in ns(u.pos)]

            if not targets:
                return None

            if unit.pos in targets:
                return unit.pos

            fps = [u.pos for u in units if u.type == unit.type]
            queue = [(0, unit.pos.imag, unit.pos.real, None, None)]
            weights = defaultdict(lambda: (inf, None, None))

            while queue:
                d, y, x, py, px = heappop(queue)
                p = x + y * 1j

                if weights[p][0] <= d:
                    continue

                weights[p] = (d, py, px)

                if d == 1:
                    py, px = y, x

                if p in targets:
                    break

                for n in ns(p):
                    if lines[int(n.imag)][int(n.real)] == '#' or n in fps:
                        continue

                    heappush(queue, (d + 1, n.imag, n.real, py, px))

            else:
                return unit.pos

            return px + py * 1j

        rounds = 0
        while True:
            units = [u for u in units if u.hp > 0]
            units = sorted(units, key=lambda u: (u.pos.imag, u.pos.real))

            if SHOW_ANIMATION:
                os.system('clear')
                print('ap =', elfap, 't =', rounds)
                ts, _, ps = zip(*units)
                for j, r in enumerate(lines):
                    line = []
                    for i, c in enumerate(r):
                        idx = next((k for k, p in enumerate(ps) if p == i + j * 1j), None)
                        if idx is not None:
                            line.append(ts[idx])
                            continue
                        line.append(c)
                    print(''.join(line))

            for idx, unit in enumerate(units):
                if unit.hp == 0:
                    continue

                _np = np(unit)

                if unit.pos != _np:
                    if _np is None:
                        return rounds, units

                    unit = unit._replace(pos=_np)
                    units[idx] = unit

                foes = [u for u in enumerate(units) if u[1].type != unit.type]
                foes = [u for u in foes if u[1].hp > 0 and u[1].pos in ns(unit.pos)]

                if not foes:
                    continue

                foes = sorted(foes, key=lambda u: (u[1].hp, u[1].pos.imag, u[1].pos.real))
                fidx, foe = foes.pop(0)
                dmg = 3 if unit.type == 'G' else elfap
                units[fidx] = foe._replace(hp=max(foe.hp - dmg, 0))

            rounds += 1


    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        lines = [list(l.strip()) for l in f.readlines()]

    Unit = namedtuple('Unit', ['type', 'hp', 'pos'])

    units = []
    for j, r in enumerate(lines):
        for i, c in enumerate(r):
            if c in ['E', 'G']:
                units.append(Unit(c, 200, i + 1j * j))
                r[i] = '.'

    eap = 3
    _units = []
    nelves = len([u for u in units if u.type == 'E'])
    while len([u for u in _units if u.type == 'E']) != nelves:
        rounds, _units = simulate(units[:], eap)
        outcome = sum(u.hp for u in _units) * rounds

        if eap == 3:
            p1 = outcome

        eap += 1

    print('P1: {}'.format(p1))
    print('P2: {}'.format(outcome))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
