import itertools
import sys

if len(sys.argv) != 3:
    print "Wrong parameters: {} <number of nodes> <output filepath>".format(__file__)
    sys.exit(1)

no = (int)(sys.argv[1])
outfile = sys.argv[2]

with open(outfile, 'w') as fp:
    for i in xrange(1, no+1):
        for j in xrange(i+1, no+1):
            fp.write("{},{}\n".format(i, j))
            fp.write("{},{}\n".format(j, i))

