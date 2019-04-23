# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []

    all_unions = []

    segments = sorted(segments, key=lambda x: x.end)

    for i in range(1, len(segments)):
        current_s = segments[i]
        prev_s = segments[i-1]
        current_range = list(range(current_s.start, current_s.end+1))
        prev_range = list(range(prev_s.start, prev_s.end+1))
        union = list(set(prev_range) & set(current_range))
        union.sort()
        all_unions.append(union)

    for j in range(1, len(all_unions)):
        print(all_unions[j-1], all_unions[j])
        print(list(set(all_unions[j-1]) & set(all_unions[j])))
        # if list(set(all_unions[j-1]) & set(all_unions[j])) == []:
        #     points.append(all_unions[j-1][-1])
        # else:
        #     points.append(all_unions[j][-1])
        
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
    print('\n')
