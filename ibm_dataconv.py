import itertools
import sys
import os

def ibmdata_convert(infile, outfile, linktype):
    # create output folder if not exists
    directory = os.path.dirname(os.path.abspath(outfile))
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(infile, 'r') as rfp:
        with open(outfile, 'w') as wfp:
            for line in rfp:
                tran = list({x.strip() for x in line.split(',')})
                for i in xrange(len(tran)):
                    for j in xrange(i+1, len(tran)):
                        wfp.write("{},{}\n".format(tran[i], tran[j]))
                        if linktype[0] == "b":
                            wfp.write("{},{}\n".format(tran[j], tran[i]))
            
def main():
    if len(sys.argv) != 4:
        print "Wrong parameters: {} <in filepath> <output filepath> <directed | bidirected>".format(__file__)
        sys.exit(1)

    # get positional arguments
    infile = sys.argv[1]
    outfile = sys.argv[2]
    linktype = sys.argv[3]

    # set output filename
    ext_index = outfile.index(".")
    if linktype[0] == "b":
        outfile = outfile[:ext_index] + "_b" + outfile[ext_index:]
    elif linktype[0] == "d":
        outfile = outfile[:ext_index] + "_d" + outfile[ext_index:]
    else:
        print "Error link type!"
        sys.exit(1)

    ibmdata_convert(infile, outfile, linktype)
    
if __name__ == '__main__':
    main()
