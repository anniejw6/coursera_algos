from percolation import Percolation

files = ['greeting57.txt', 'heart25.txt',
         'input1-no.txt', 'input1.txt',
         'input10-no.txt', 'input10.txt',
         'input2-no.txt', 'input2.txt',
         'input20.txt', 'input3.txt',
         'input4.txt', 'input5.txt',
         'input50.txt', 'input6.txt',
         'input7.txt', 'input8-no.txt',
         'input8.txt', 'jerry47.txt',
         'sedgewick60.txt', 'wayne98.txt']

fails = ['greeting57.txt', 'heart25.txt', 'input1-no.txt',
		 'input2-no.txt', 'input8-no.txt', 'input10-no.txt']


def test_percolate(file_name):
    with open('./percolation/%s' % file_name) as f:
        a = [line.strip().split() for line in f]
    q = Percolation(int(a[0][0]))
    for x in a[1:]:
    	if len(x) == 2:
    		q.open(int(x[0]), int(x[1]))
    return q.percolates()

res = [test_percolate(f) == (f not in fails) for f in files]

print(res)