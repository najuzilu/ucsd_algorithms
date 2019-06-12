# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(s):
	p = []
	s = sorted(s, key=lambda x: x.end)
	for i in range(0, len(s)):
		if i == 0:
			p.append(s[i].end)
		else:
			if s[i].start <= p[-1] and s[i].end >= p[-1]:
				continue
			else:
				p.append(s[i].end)
	return p

if __name__ == '__main__':
	input = sys.stdin.read()
	n, *data = map(int, input.split())
	segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
	points = optimal_points(segments)
	print(len(points))
	for p in points:
		print(p, end=' ')