from scipy.sparse import csr_matrix
import numpy as np
import sys

C = 0.5

def simrank(csr_links, c, a, b, rest_step=5):
    """
    Simrank algorithm
    Notice: a & b are id not item string
    """
    # prevent endless loop
    if rest_step==0:
        # print "rest_step limitation occured!"
        return 0
    if a == b:
        return 1.0
    _, a_inlist = csr_links.T[a].nonzero()
    _, b_inlist = csr_links.T[b].nonzero()

    ret = 0
    denum = len(a_inlist)*len(b_inlist)
    for ai in a_inlist:
        for bi in b_inlist:
            ret = ret + 1.0 * c * simrank(csr_links, c, ai, bi, rest_step-1) / denum
    return ret
        
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

def show_results(csr_links, id_dict):
    print "C = {}".format(C)
    print "=======\n"
    keys = id_dict.keys()
    keys.sort()
    for i in xrange(len(keys)):
        for j in xrange(i+1, len(keys)):
            a = keys[i]
            b = keys[j]
            print "S({}, {}): {}".format(a, b, simrank(csr_links, C, id_dict[a], id_dict[b]))

def main():
    if len(sys.argv) != 2:
        print "Wrong parameters: {} <filepath>".format(__file__)
        sys.exit(1)
    filepath = sys.argv[1]

    data, id_dict = read_data(filepath)
    csr_links = to_csr(data, id_dict)
    show_results(csr_links, id_dict)

if __name__ == '__main__':
    main()
