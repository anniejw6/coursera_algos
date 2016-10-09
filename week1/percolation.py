""" Percolation homework assignment"""

import numpy as np
import random as rand
import pprint


class PercolationStats:
    """Class representation of percolation"""

    def __init__(self, n, trials, seed=1234):

        assert n > 0, 'n must be greater than 0'
        assert trials > 0, 'trials must be greater than 0'
        self.n = n
        self.trials = trials
        self.seed = seed

    def __str__(self):
        res = dict(
            a_mean=self.mean,
            b_stdev=self.stdev,
            c_conf=(self.confLo, self.confHi),
            d_config=dict(n=self.n,
                          num_trials=self.trials,
                          seed=self.seed)
        )
        return pprint.pformat(res)

    def _run_trial(self, seed, verbose=False):
        """run a trial"""

        rand.seed(seed)
        trial = Percolation(self.n)

        if verbose:
            counter = 0

        while trial.percolates() != True:
            if verbose:
                counter = counter + 1
                if counter % 50 == 0:
                    print('%s is the counter and %s are open' %
                          (counter, sum(trial.arr_open)))
            trial.open(rand.randint(1, self.n), rand.randint(1, self.n))
        return sum(trial.arr_open) / (self.n**2)

    def run_trials(self):

        sums = [self._run_trial(x) for x in
                range(self.seed, self.seed + self.trials)]

        self.mean = np.mean(sums)
        self.stdev = np.std(sums) / np.sqrt(self.trials)
        self.confLo = self.mean - 1.96 * self.stdev
        self.confHi = self.mean + 1.96 * self.stdev

        print('Finished runs')


class Percolation:

    """ Class representation of percolation"""

    def __init__(self, n):

        self.n = n
        # array to store whether sites are open or closed
        self.arr_open = np.array([False] * n**2)
        # store array for quick union
        self.qu = quickUnion(n**2 + 2)  # add two virtual sites
        self.vstr_index = len(self.qu.array) - 2
        self.vend_index = len(self.qu.array) - 1

    def __str__(self):
        """view the matrix"""
        return str(np.mat(self.qu.array[:-2]).reshape(self.n, self.n))

    def _isvalid(self, x):
        """ check if i or j term is valid"""
        return (x <= self.n) & (x > 0)

    def _index(self, i, j):
        """generate array index from i, j term"""
        assert self._isvalid(i), 'i term (%s) is out of bounds' % i
        assert self._isvalid(j), 'j term (%s) is out of bounds' % j

        return self.n * (i - 1) + (j - 1)

    def open(self, i, j):
        """ Open up a site """
        if not self.isOpen(i, j):
            # set open to true
            self.arr_open[self._index(i, j)] = True
            # connect to surrounding sites
            [self.qu.union(self._index(i, j), self._index(x[0], x[1]))
                for x in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]
                if self.isOpen(x[0], x[1])]

    def isOpen(self, i, j):
        """ Check if site is open"""
        if self._isvalid(i) & self._isvalid(j):
            return self.arr_open[self._index(i, j)]
        return False

    def _connect(self, t):
        assert (t in ['start', 'end']), "type not valid"
        if t == 'start':
            row = 1
            vindex = self.vstr_index
        else:
            row = self.n
            vindex = self.vend_index

        # connect
        [self.qu.union(vindex, self._index(x[0], x[1]))
            for x in [(row, z) for z in range(1, self.n + 1)]
            if self.isOpen(x[0], x[1])]

    def isFull(self, i, j):
        """ Check if site can connect to virtual start"""
        self._connect('start')
        return self.qu.connected(self.vstr_index, self._index(i, j))

    def percolates(self):
        """ Check if percolated"""
        self._connect('start')
        self._connect('end')
        return self.qu.connected(self.vstr_index, self.vend_index)


class quickUnion:
    """Class representation of quick union algorithm"""

    def __init__(self, n):

        assert (n > 0), 'n is too low'

        self.n = n
        self.array = np.array(range(0, n))
        self.tree_size = [1] * n

    def root(self, x):
        """ find root of array index """
        assert ((x < self.n) & (x >= 0)), 'array index is out of bounds'

        while x != self.array[x]:
            self.array[x] = self.array[self.array[x]]
            x = self.array[x]
        return x

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
        """ check if two values are connected """
        return self.root(p) == self.root(q)

if __name__ == '__main__':
    #q = PercolationStats(n=200, trials=5, seed=1111)
    #print(q._run_trial(seed=1234, verbose=True))
    # q.run_trials()
    # print(q)

    #q = PercolationStats(n=2, trials=10000, seed=1111)
    #print(q._run_trial(seed = 1234))
    # q.run_trials()
    # print(q)

    zz = Percolation(15)
    zz.open(1, 3)
    zz.open(2, 4)
    zz.open(2, 5)
    zz.open(1, 5)
    print(zz)
