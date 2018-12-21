#! /usr/bin/env python3

import os
import sys

from time import process_time

def exec(cmd):
    def a(regs, instr):
        after = regs[:]
        after[instr[2]] = cmd(regs, instr[0], instr[1])
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
    'gtir': exec(lambda regs, a, b: int(a > regs[b])),
    'gtri': exec(lambda regs, a, b: int(regs[a] > b)),
    'gtrr': exec(lambda regs, a, b: int(regs[a] > regs[b])),
    'eqir': exec(lambda regs, a, b: int(a == regs[b])),
    'eqri': exec(lambda regs, a, b: int(regs[a] == b)),
    'eqrr': exec(lambda regs, a, b: int(regs[a] == regs[b])),
}

def main():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        instructions = [l.strip() for l in f.readlines()]

    def run(regs):
        _is = instructions[:]
        ip = 0
        ipreg = None

        while True:
            instr = _is[ip]
            if instr.startswith('#ip'):
                ipreg = int(instr.split(' ')[1])
                _is = [i for i in instructions if i != instr]
                continue

            regs[ipreg] = ip

            cmd, *args = instr.split(' ')
            args = [int(arg) for arg in args]
            regs = cmds[cmd](regs, args)

            ip = regs[ipreg]
            ip += 1

            if ip == 3 and regs[5] > 0:
                if regs[1] % regs[5] == 0:
                    regs[0] += regs[5]

                regs[4] = 0
                regs[3] = regs[1]
                ip = 12

            if ip < 0 or ip >= len(_is):
                break

        return regs[0]

    print('P1: {}'.format(run([0, 0, 0, 0, 0, 0])))
    print('P2: {}'.format(run([1, 0, 0, 0, 0, 0])))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
