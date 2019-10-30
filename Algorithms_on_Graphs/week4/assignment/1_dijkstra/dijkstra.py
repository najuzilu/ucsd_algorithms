#Uses python3

import sys
import queue
import heapq
from heapq import heapify, heappush, heappop,  _siftup, _siftdown

def distance_(adj, cost, s, t):
	distance = [float("inf") for _ in range(len(adj))]
	previous = [None for _ in range(len(adj))]

	### initialize queue with starting node
	myQueue = queue.PriorityQueue(maxsize = len(adj))
	myQueue.put((0, s)) # priority first, then node value
	distance[s] = 0

	while not myQueue.empty():
		minValue = myQueue.get() # get node with min cost
		costMinValue = minValue[0] # cost of the node
		nodeMinValue = minValue[1] # actual node number 

	# 	# for edge in minNode
		for i in range(len(adj[nodeMinValue])):
			edgeNode = adj[nodeMinValue][i]
			edgeCost = cost[nodeMinValue][i]

			if distance[edgeNode] > distance[nodeMinValue] + edgeCost:
				distance[edgeNode] = distance[nodeMinValue] + edgeCost
				previous[edgeNode] = nodeMinValue
				myQueue.put((distance[edgeNode], edgeNode)) #(distance[edgeNode], edgeNode)

	if distance[t] < float("inf"):
		return distance[t]
	else:
		return -1

def distance(adj, cost, s, t):
	# print("adj={}, cost={}, s={}, t={}\n".format(adj, cost, s, t))
	distance = [float("inf") for _ in range(len(adj))]
	previous = [None for _ in range(len(adj))]

	### initialize queue with starting node
	myQueue = []
	distance[s] = 0

	### make queue from all nodes
	for j in range(len(adj[s])):
		distance[adj[s][j]] = cost[s][j]
		previous[adj[s][j]] = s
		heapq.heappush(myQueue, (cost[s][j], adj[s][j]))

	while myQueue:
		### extract min value of queue
		minValue = heapq.heappop(myQueue)
		costMinValue = minValue[0] # cost of the node
		nodeMinValue = minValue[1] # actual node number

		# print(">> previous[minValue]=", previous[nodeMinValue])
		# print("minValue={}, myQueue={}".format(minValue, myQueue))

		### for all edges in minValue
		for i in range(len(adj[nodeMinValue])):
			edgeNode = adj[nodeMinValue][i]
			edgeCost = cost[nodeMinValue][i]

			node = (edgeCost, edgeNode)
			
			# print("     node={}, distance={}, previous={}, distance[edgeNode] > distance[nodeMinValue] + edgeCost = {} > {} + {} ".format(node, distance, previous, distance[edgeNode], distance[nodeMinValue], edgeCost))

			if distance[edgeNode] > distance[nodeMinValue] + edgeCost:
				heapq.heappush(myQueue, node)
				distance[edgeNode] = distance[nodeMinValue] + edgeCost
				previous[edgeNode] = nodeMinValue

				newNode = (distance[edgeNode], edgeNode)
				i = myQueue.index(node)
				myQueue[i] = newNode
				heapq.heapify(myQueue)
				# print("     >QUEUE={}, PREVIOUS:{}, distance={} ".format(myQueue, previous, distance))
	if distance[t] < float("inf"):
		return distance[t]
	else:
		return -1

if __name__ == '__main__':
	input = sys.stdin.read()
	data = list(map(int, input.split()))
	n, m = data[0:2]
	data = data[2:]
	edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
	data = data[3 * m:]
	adj = [[] for _ in range(n)]
	cost = [[] for _ in range(n)]
	for ((a, b), w) in edges:
		adj[a - 1].append(b - 1)
		cost[a - 1].append(w)
	s, t = data[0] - 1, data[1] - 1
	print(distance(adj, cost, s, t))
