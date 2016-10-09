import numpy as np 

class UF:
	""" class for UF object """

	def __init__(self, length):
		self.array = np.array(range(0, length + 1))

	def connected(self, p, q):
		# Adding -1 because Python is 0-indexed
		return self.array[p - 1] == self.array[q - 1]

	def union(self, p, q):
		self.array[self.array == self.array[q - 1]] = self.array[p - 1]


if __name__ == '__main__':
	z = UF(5)
	print(z.connected(1,2))
	z.union(1,2)
	print(z.connected(1, 2))
	print(z.array)