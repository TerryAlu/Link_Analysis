from scipy.sparse import csr_matrix
import numpy as np

EPSILON = 0.01

def hits(csr_links):
    """
    HITS algorithm
    """
    # init authority and hubness vector
    l, _ =  csr_links.shape
    auth = np.ones(l)
    hub = np.ones(l)
    # init in and out matrix
    out_csr = csr_links
    in_csr = csr_links.transpose()

    while True:
        # caluculate next auth. and hub
        n_auth = in_csr.dot(hub)
        n_hub = out_csr.dot(auth)

        # normalization
        n_auth = normalize(n_auth)
        n_hub = normalize(n_hub)

        delta = vector_distance(n_auth, auth) + vector_distance(n_hub, hub)

        # update auth. and hub
        auth = n_auth
        hub = n_hub

        # do until delta < EPSILON
        if delta <= EPSILON:
            break

    return auth, hub

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

def normalize(vec):
    """
    one-norm normalization
    """
    acc = sum(vec)
    if acc == 0:
        return vec
    else:
        return 1.0*np.array(vec)/acc

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

def show_results(auth, hub):
    print ">> Authority <<"
    print auth
    print ""
    print ">> Hubness <<"
    print hub

def main():
    data, id_dict = read_data("hw3dataset/graph_7.txt")
    csr_links = to_csr(data, id_dict)
    auth, hub = hits(csr_links)
    show_results(auth, hub)

if __name__ == '__main__':
    main()
