# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def in_list(list_, list_points):
	flag = False
	for each in list_:
		if each in list_points:
			flag = True
	return flag


def optimal_points(segments):
	points = []
	segments = sorted(segments, key=lambda x: x.end)

	segments.append(segments[-1])

	for i in range(1, len(segments)): #len(segments)
		current_s = segments[i]
		prev_s = segments[i-1]
		current_range = list(range(current_s.start, current_s.end+1))
		prev_range = list(range(prev_s.start, prev_s.end+1))

		print(current_range)

		if in_list(prev_range, points):
		    continue
		union = list(set(prev_range) & set(current_range))
		print('{}-{} >> union: {}, points: {}'.format(prev_range, current_range, union, points))
		if union != []:
			union.sort()
			points.append(union[-1])
		else:
			if prev_range[-1] not in points:
				points.append(prev_range[-1])
			if current_range[-1] not in points:
				points.append(current_range[-1])
	return points

if __name__ == '__main__':
	input = sys.stdin.read()
	n, *data = map(int, input.split())
	segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
	points = optimal_points(segments)
	print(len(points))
	for p in points:
		print(p, end=' ')
