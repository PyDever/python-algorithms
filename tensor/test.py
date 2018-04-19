

import math
from operator import itemgetter

class Graph(object):
	def __init__(self):
		self.Nodes = {};
	def addNode(self,  node, inputx):
		self.Nodes[node] = inputx
	def computateNode(self, node):
		try:
			for k, v in self.Nodes.items():
				if k==node:
					op = v[0]
					print(op, v[1:])
		except:
			print('[!] Error.')
	def visualizeNodes(self):
		try:
			for k, v in self.Nodes.items():
				op = v[0]
				c = 0
				if op=='+':
					c += 1
				elif op=='*':
					c += 2
				elif op=='-':
					c += 3
				elif op=='/' or '//' or '%':
					c += 4
				out = k
				print('	'*c, op, v[1:], out)
		except:
			print('[!] Error.')
	def computateNodes(self, nodes):
		results = []
		for node in nodes:
			for k, v in self.Nodes.items():
				if k==node:
					op = v[0]
					R = []
					R.append(op)
					R.append(v[1:])
					results.append(tuple(R))
		print(results)

	

g = Graph()
g.addNode(6, ['+', 3, 3])
g.addNode(5, ['+', 2, 3])
g.addNode(20, ['*', 10, 2])
g.addNode(10, ['*', 5, 2])
g.addNode(1, ['/', 90, 90])
g.computateNodes((6, 5, 1))

