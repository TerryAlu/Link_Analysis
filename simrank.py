import numpy as np
import sys

C = 0.5
EPSILON = 0.001

def simrank(links, c):
    """
    Simrank algorithm
    """
    assert c < 1

    # get indicator vector for elements with zero in-degree
    _, n = links.shape
    zero_inlist = []
    for x in xrange(n):
        inlist = links.T[x].nonzero()[0]
        zero_inlist.append(True if len(inlist)==0 else False)

    ranks = np.identity(n)
    n_ranks = np.identity(n)

    print "delta of each iterations: "
    
    # update
    while True:
        # from (i, j)
        for i in xrange(n):
            for j in xrange(n):
                # to (x, y)
                for x in links[i].nonzero()[0]:
                    for y in links[j].nonzero()[0]:
                        if x == y:
                            continue
                        # propagate similarity
                        n_ranks[x][y] = n_ranks[x][y] + ranks[i][j]

        # n_ranks * c / (in-degree(i)*in-degree(j))
        for i in xrange(n):
            for j in xrange(n):
                if i == j:
                    continue
                i_in_count = len(links.T[i].nonzero()[0])
                j_in_count = len(links.T[j].nonzero()[0])
                if i_in_count==0 or j_in_count==0:
                    continue
                n_ranks[i][j] = 1.0 * c * n_ranks[i][j] / (i_in_count * j_in_count)

        delta = abs(np.sum(n_ranks)-np.sum(ranks))
        print delta
        if delta <= EPSILON:
            print ""
            break
        ranks = n_ranks.copy()
        n_ranks = np.identity(n)

    return n_ranks
        
def to_matrix(data, id_dict):
    """
    Convert dict. data to csr format
    """
    dense = np.zeros((len(id_dict), len(id_dict)))
    for k, v in data.iteritems():
        for x in v:
            # create link
            dense[id_dict[k]][id_dict[x]] = 1
    return dense

def read_data(filepath):
    """
    Read data from database
    """
    data = {}
    with open(filepath) as fp:
        for line in fp:
            x, y = line.strip().split(',')
            if x not in data:
                data[x] = []
            if y not in data:
                data[y] = []
            data[x].append(y)

    # Assign id for each item
    id_dict = {}
    i = 0
    keys = data.keys()
    keys.sort()
    for x in keys:
        id_dict[x] = i
        i = i+1
    return data, id_dict

def show_results(ranks, id_dict):
    print "C = {}".format(C)
    print "=======\n"
    keys = id_dict.keys()
    keys.sort()
    for i in xrange(len(keys)):
        for j in xrange(i, len(keys)):
            a = keys[i]
            b = keys[j]
            print "S({}, {}): {}".format(a, b, ranks[i][j])
    # print ""
    # print ranks

def main():
    if len(sys.argv) != 2:
        print "Wrong parameters: {} <filepath>".format(__file__)
        sys.exit(1)
    filepath = sys.argv[1]

    data, id_dict = read_data(filepath)
    links = to_matrix(data, id_dict)
    ranks = simrank(links, C)
    show_results(ranks, id_dict)

if __name__ == '__main__':
    main()
