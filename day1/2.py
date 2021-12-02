#!/usr/bin/env python3

with open('input') as f:
    depth_increased_count: int = 0
    last = None

    lines = []
    with open('input') as f:
        for line in f.readlines():
            lines.append(int(line.strip()))

    #for line in lines:
    #    if last is not None:
    #        if int(line) > last:
    #            depth_increased_count += 1

    #    last = int(line)

    for i, _ in enumerate(lines):
        window1 = sum(lines[i:i+3])
        window2 = sum(lines[i+1:i+4])

        if window1 < window2:
            depth_increased_count += 1

    print(depth_increased_count)

