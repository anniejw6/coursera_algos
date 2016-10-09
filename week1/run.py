from percolation import PercolationStats

q = PercolationStats(n=200, trials=5, seed=1111)
print(q._run_trial(seed=1234, verbose=True))