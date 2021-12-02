#!/usr/bin/env python3

with open('input') as f:
    depth_increased_count: int = 0
    last = None

    lines = []
    with open('input') as f:
        for line in f.readlines():
            lines.append(line.strip())

    for line in lines:
        if last is not None:
            if int(line) > last:
                depth_increased_count += 1

        last = int(line)

    print(depth_increased_count)

