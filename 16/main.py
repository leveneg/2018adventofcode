#! /usr/bin/env python3

import os
import sys

from collections import defaultdict
from time import process_time

def exec(cmd):
    def a(regs, instr):
        after = regs[:]
        after[instr[3]] = cmd(regs, instr[1], instr[2])
        return after
    return a

cmds = {
    'addr': exec(lambda regs, a, b: regs[a] + regs[b]),
    'addi': exec(lambda regs, a, b: regs[a] + b),
    'mulr': exec(lambda regs, a, b: regs[a] * regs[b]),
    'muli': exec(lambda regs, a, b: regs[a] * b),
    'banr': exec(lambda regs, a, b: regs[a] & regs[b]),
    'bani': exec(lambda regs, a, b: regs[a] & b),
    'borr': exec(lambda regs, a, b: regs[a] | regs[b]),
    'bori': exec(lambda regs, a, b: regs[a] | b),
    'setr': exec(lambda regs, a, b: regs[a]),
    'seti': exec(lambda regs, a, b: a),
    'gtir': exec(lambda regs, a, b: a > regs[b]),
    'gtri': exec(lambda regs, a, b: regs[a] > b),
    'gtrr': exec(lambda regs, a, b: regs[a] > regs[b]),
    'eqir': exec(lambda regs, a, b: a == regs[b]),
    'eqri': exec(lambda regs, a, b: regs[a] == b),
    'eqrr': exec(lambda regs, a, b: regs[a] == regs[b]),
}

def main():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        samples, prog = f.read().strip().split('\n\n\n')
        samples = [l for l in samples.split('\n') if l is not '']
        prog = [[int(c) for c in l.split(' ')] for l in prog.strip().split('\n')]

    p1 = 0
    codes = defaultdict(set)
    for before, instr, after in zip(*[iter(samples)]*3):
        before = [int(c) for c in before.split(': ')[1].strip('[]').split(', ')]
        instr = [int(c) for c in instr.split(' ')]
        after = [int(c) for c in after.split(':  ')[1].strip('[]').split(', ')]

        cands = []
        for op, fn in cmds.items():
            if fn(before, instr) == after:
                cands.append(op)
                codes[instr[0]].add(op)

                if len(cands) >= 3:
                    p1 += 1
                    break

    while not all(type(v) is str for v in codes.values()):
        code, instr = next((k, v) for k, v in codes.items() if len(v) == 1)

        for k, v in codes.items():
            if k != code and type(v) is set: v -= v & instr

        codes[code] = instr.pop()

    regs = [0, 0, 0, 0]
    for op in prog:
        regs = cmds[codes[op[0]]](regs, op)

    p2 = regs[0]

    print('P1: {}'.format(p1))
    print('P2: {}'.format(p2))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
