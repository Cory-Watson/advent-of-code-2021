#!/usr/bin/env python3

position = {
        'depth': 0,
        'horizontal': 0,
        'aim': 0
        }

lines = []
with open('input') as f:
    for line in f.readlines():
        lines.append(line.split())

for direction, count in lines:
    if direction == 'forward':
        position['horizontal'] += int(count)
        position['depth'] += position['aim'] * int(count)
    elif direction == 'down':
        #position['depth'] += int(count)
        position['aim'] += int(count)
    elif direction == 'up':
        #position['depth'] -= int(count)
        position['aim'] -= int(count)

print(position)
print('depth * horizontal = {}'
      .format(position['depth'] * position['horizontal']))
