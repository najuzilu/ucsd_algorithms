# python3
import sys

# python car_fueling.py < tests/1

def compute_min_refills(distance, tank, stops):
	stops = [0] + stops + [distance]

	numRefills = 0
	currentRefillIndex = 0

	while currentRefillIndex <= len(stops)-2:
		lastRefillIndex = currentRefillIndex

		while (currentRefillIndex <=  len(stops)-2) and (stops[currentRefillIndex+1]-stops[lastRefillIndex] <= tank):
			currentRefillIndex += 1

		if currentRefillIndex == lastRefillIndex:
			return -1

		if currentRefillIndex <= len(stops)-2:
			numRefills += 1
	return numRefills


if __name__ == '__main__':
	d, m, _, *stops = map(int, sys.stdin.read().split())
	print(compute_min_refills(d, m, stops))
