

EXAMPLE = 'ilustreWebTest.20110805.soqrates.SS.trdmsq_wait'

def example(x):

    nametoks = x.split('.')
    
    d = None
    
    lastn = None
    for name in nametoks:
        print name
        n = {}
        n['id'] = name
        n['children'] = []

        print n

        if d == None:
            d = n
        else:
            lastn['children'].append(n)
        
        lastn = n

    return d


if __name__ == '__main__':
    x = example(EXAMPLE)
    #file_ = '/Users/ilustre/development/repo/jittest/jobs.txt'

    #with open(file_, 'r') as fh:
    #    
    #    thedict={}
    #    for line in fh.readlines():
    #        line = line.strip()
    #        linetoks = line.split(' ')
    #        name = linetoks[1]
    #        print name

    #        nametoks = name.split('.')
    #        
    #        parentname = None
    #        for tok in nametoks:
    #            print 'Parent=%s, child=%s' % (parentname, tok)
    #            parentnode = thedict[parentname] if parentname in thedict else None
    #            if parentnode != None:
    #                parentnode.append(tok)
    #            else:
    #                thedict[tok] = []

    #            parentname = tok
