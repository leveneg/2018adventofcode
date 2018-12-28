#! /usr/bin/env python3

import os
import sys

from collections import namedtuple
from math import ceil
from time import process_time

Group = namedtuple(
    'Group',
    [
        'gtype',
        'nunits',
        'hpoints',
        'atype',
        'adamage',
        'immunities',
        'weaknesses',
        'initiative'
    ]
)

def main():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        lines = [l.strip() for l in f.readlines()]

    gtypes = ['Immune System', 'Infection']
    atypes = ['radiation', 'fire', 'cold', 'slashing', 'bludgeoning']

    groups = []
    gtype = None
    for line in lines:
        if not line: continue

        if line.strip(':') in gtypes:
            gtype = gtypes.index(line.strip(':'))
            continue

        parts = line.split(' ')
        nu = int(parts[0])
        hp = int(parts[4])
        ad = int(parts[parts.index('does') + 1])
        at = atypes.index(parts[parts.index('does') + 2])
        init = int(parts[-1])

        weaknesses = []
        immunities = []
        astr = line[line.find('('):line.find(')')][1:]

        for attr in astr.split('; '):
            if not attr: continue
            atype = immunities if attr.startswith('immune') else weaknesses
            for atk in attr.split()[2:]:
                atype.append(atypes.index(atk.strip(',')))

        groups.append(Group(gtype, nu, hp, at, ad, immunities, weaknesses, init))

    def fight(groups, boost):
        for i, group in enumerate(groups):
            if group.gtype == 0:
                groups[i] = group._replace(adamage=group.adamage + boost)

        while True:
            selections = []
            groups = sorted(
                groups,
                key=lambda g:(-g.nunits * g.adamage, -g.initiative)
            )

            for i, group in enumerate(groups):
                selection, maxdamage = None, None
                for j, cand in enumerate(groups):
                    if cand.gtype == group.gtype:
                        continue

                    if cand.nunits == 0:
                        continue

                    if j in selections:
                        continue

                    mult = 2 if group.atype in cand.weaknesses else 1
                    mult = 0 if group.atype in cand.immunities else mult
                    damage = mult * group.nunits * group.adamage

                    if not damage:
                        continue

                    if selection is not None and damage < maxdamage:
                        continue

                    if selection is not None and damage == maxdamage:
                        s = groups[selection]
                        sep = s.nunits * s.adamage
                        cep = cand.nunits * cand.adamage

                        if sep > cep:
                            continue

                        if sep == cep and cand.initiative < s.initiative:
                            continue

                    selection = j
                    maxdamage = damage

                selections.append(selection)

            if not any(selections):
                return [sum(g.nunits for g in groups if g.gtype == i) for i in [0, 1]]

            units_killed = False
            for i, _ in sorted(enumerate(groups), key=lambda g: -g[1].initiative):
                sidx = selections[i]

                if sidx is None:
                    continue

                _g = groups[i]
                opp = groups[sidx]
                mult = 2 if _g.atype in opp.weaknesses else 1
                mult = 0 if _g.atype in opp.immunities else mult
                damage = mult * _g.nunits * _g.adamage
                nunits = max(ceil(opp.nunits - damage / opp.hpoints), 0)

                if nunits == opp.nunits:
                    continue

                groups[sidx] = opp._replace(nunits=nunits)
                units_killed = True

            if not units_killed:
                return [sum(g.nunits for g in groups if g.gtype == i) for i in [0, 1]]

    boost = 0
    while True:
        result = fight(groups[:], boost)

        if boost == 0:
            print('P1: {}'.format(sum(result)))

        if result[1] == 0:
            break

        boost += 1

    print('P2: {}'.format(sum(result)))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
