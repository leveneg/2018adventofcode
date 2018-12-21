#! /usr/bin/env python3

from time import process_time

def main():
    r3 = 0
    seen = []
    p1 = p2 = None
    mask = 1 << 24

    while not p2:
        r2 = r3 | 65536
        r3 = 1505483

        while True:
            r3 = (((r3 + (r2 % 256)) % mask) * 65899) % mask

            if 256 > r2:
                if not p1: p1 = r3

                if r3 in seen:
                    p2 = seen[-1]

                seen.append(r3)
                break
            else:
                r2 //= 256


    print('P1: {}'.format(p1))
    print('P2: {}'.format(p2))

if __name__ == "__main__":
    start = process_time()
    main()
    print('--- {} seconds ---'.format(process_time() - start))
