#! /usr/bin/env python3

import os
import sys

from collections import defaultdict
from time import process_time

def getLogs():
    with open(os.path.join(sys.path[0], 'input.txt')) as f:
        for line in f:
            ts, desc = line.strip().split('] ')
            date, time = ts.lstrip('[').split(' ')
            (_, month, day) = map(int, date.split('-'))
            (hour, minute) = map(int, time.split(':'))

            yield (month, day, hour, minute, desc)

def main():
    entries = sorted(list(getLogs()))
    guard = None
    asleep_at = None
    sleeps = defaultdict(lambda: [0 for _ in range(60)])

    for entry in entries:
        month, day, hour, minute, desc = entry

        if desc.startswith('Guard'):
            guard = desc.split(' ')[1]
            continue

        if desc == 'falls asleep':
            asleep_at = minute
            continue

        if desc == 'wakes up':
            for m in range(asleep_at, minute):
                sleeps[guard][m] += 1

    for part, func in [('P1', sum), ('P2', max)]:
        guard, minutes = max(sleeps.items(), key=lambda x: func(x[1]))
        minute = minutes.index(max(minutes))
        print('{}: {}'.format(part, (int(guard.lstrip('#')) * minute)))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
