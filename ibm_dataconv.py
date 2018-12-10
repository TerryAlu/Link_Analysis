import itertools
import sys

def ibmdata_convert(infile, outfile):
    with open(infile, 'r') as rfp:
        with open(outfile, 'w') as wfp:
            for line in rfp:
                tran = list({x.strip() for x in line.split(',')})
                for i in xrange(len(tran)):
                    for j in xrange(i+1, len(tran)):
                        wfp.write("{},{}\n".format(tran[i], tran[j]))
                        wfp.write("{},{}\n".format(tran[j], tran[i]))
            
def main():
    if len(sys.argv) != 3:
        print "Wrong parameters: {} <in filepath> <output filepath>".format(__file__)
        sys.exit(1)

    infile = sys.argv[1]
    outfile = sys.argv[2]
    ibmdata_convert(infile, outfile)
    
if __name__ == '__main__':
    main()
