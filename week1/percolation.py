import numpy as np

# create N x N array of index
# create N x N array of open/closed
# create virtual site

# randomly close one block
# check

# Error:
# if any argument to open(), isOpen(), or isFull() is outside its prescribed range.
# The constructor should throw a java.lang.IllegalArgumentException if n ≤ 0.


class PercolationStats:
    """Class representation of percolation"""

    def __init__(self, n, trials):

        self.n = n
        self.trials = trials

    def run_trial(self):
    	qu = quickUnion(self.n**2 + 2)  # for two virtualobj
    	# self.mean = 
    	# self.stdev =
    	# self.confidenceLo =
    	# self.confidenceHi = 
        self.vstr_index = len(self.qu.array) - 2  # index of start virtual site
        self.vend_index = len(self.qu.array) - 1  # index of ending virtual site
    
    def close(self):


    def find_path(self):
        # union virtual sites
        [self.qu.union(self.vstr_index, x) for x in range(0, n)]
        [self.qu.union(self.vend_index, x) for x in range(n * (n - 1), n**2)]

class Percolation:

	def __init__(self, n):

		self.n = n
		self.as_array = quickUnion(n**2 + 2)

    def open(self, i, j):
    	pass

    def isOpen(self, i, j):
    	pass

    def isFull(self, i, j):
    	pass

    def percolates(self):
    	pass


class quickUnion:
    """Class representation of quick union algorithm"""

    def __init__(self, n):

        assert (n > 0), 'n is too low'

        self.n = n
        self.array = np.array(range(0, n))
        self.tree_size = [1] * n

    def root(self, x):
        assert ( (x < self.n) & (x >= 0) ) , 'array index is out of bounds'

        while(x != self.array[x]):
            self.array[x] = self.array[self.array[x]]
            x = self.array[x]
        return(x)

    def union(self, p, q):

        p = self.root(p)
        q = self.root(q)

        # determine which tree is larger
        # join smaller tree to larger tree
        # updates sizes
        if self.tree_size[p] < self.tree_size[q]:
            self.array[p] = q
            self.tree_size[q] = self.tree_size[q] + self.tree_size[p]
        else:
            self.array[q] = p
            self.tree_size[p] = self.tree_size[q] + self.tree_size[p]

    def connected(self, p, q):

        return(self.root(p) == self.root(q))

if __name__ == '__main__':
    q = quickUnion(5)
    q.union(1, 3)
    q.union(1, 2)
    print(q.array)
    print(q.connected(2, 3))

    q = Percolate(5)
    print(q.qu.array)
