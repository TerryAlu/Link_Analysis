from scipy.sparse import csr_matrix
import numpy as np

EPSILON = 0.0001

def pagerank(csr_links, d):
    """
    PageRank Algorithm
    """
    assert d>=0 and d<=1
    n, _ =  csr_links.shape
    sink, tm, jump = prepare_matrices(csr_links)

    pr = np.array([1.0/n]*n)
    while True:
        # update page rank
        n_pr = d*jump.dot(pr) + (1.0-d)*sink.dot(pr) + (1.0-d)*tm.T.dot(pr)

        # check breakout condition
        delta = vector_distance(n_pr, pr)
        pr = n_pr
        if delta <= EPSILON:
            break
    return pr
        
def vector_distance(a, b):
    """
    Return the distance between two vectors
    """
    if not len(a) == len(b):
        raise Exception("length of two vectors are not equal")

    delta = 0
    for i in xrange(len(a)):
        delta = abs(a[i]-b[i])
    return delta

def prepare_matrices(csr_links):
    """
    Return sink, transient and jump matrices
    """
    n, _ =  csr_links.shape

    # sink matrix
    sink_sum = csr_links.sum(1)
    sink = np.array([[1.0/n]*n if x==0 else [0]*n for x in np.nditer(sink_sum)])

    # transient matrix
    tm = np.array(csr_links.todense())
    for i, row in enumerate(tm):
        if sink_sum[i] > 0:
            tm[i] = tm[i] / sink_sum[i]

    # jump matrix
    jump = np.full((n,n), 1.0/n)

    return sink, tm, jump

def to_csr(data, id_dict):
    """
    Convert dict. data to csr format
    """
    dense = np.zeros((len(id_dict), len(id_dict)))
    for k, v in data.iteritems():
        for x in v:
            # create link
            dense[id_dict[k]][id_dict[x]] = 1
    return csr_matrix(dense)

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

def show_results(pr):
    print ">> Page Rank <<"
    print pr

def main():
    data, id_dict = read_data("hw3dataset/graph_8.txt")
    csr_links = to_csr(data, id_dict)
    pr = pagerank(csr_links, 0.15)
    show_results(pr)

if __name__ == '__main__':
    main()
