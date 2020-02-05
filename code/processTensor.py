def readfile(file):
    f = open(file, 'r')
    lines = f.readlines()
    rows = []
    cols = []
    tslist = []
    nums = []
    for line in lines:
        words = line.strip().split(',')
        rows.append(int(words[0]))
        cols.append(int(words[1])) # concatenate items 
        tslist.append(int(words[2]))
        nums.append(int(words[3]))
    f.close()
    return rows, cols, nums, tslist


# 'delete rate'
def deleteRateFromTensor(tensor, newtensor):
    with open(tensor, 'rb') as te, open(newtensor, 'wb') as nte:
        for line in te:
            cols = line.strip().split(',')
            rate = float(cols[3])
            if rate >= 4:
                nte.write(','.join((cols[0], cols[1], cols[2], cols[4])))
                nte.write('\n')
    te.close()
    nte.close()


def sort_by_ts(initfile, sortfile, tscol=2):
    tuples = []
    with open(initfile, 'r') as inf, open(sortfile, 'w') as sortf:
        for line in inf:
            cols = line.strip().split(',')
            tup = tuple((cols[0], cols[1], int(cols[2]), cols[3]))
            tuples.append(tup)
        tuples.sort(key=lambda x: x[tscol])
        mints = tuples[0][tscol]
        for tup in tuples:
            ts = tup[tscol] - mints
            sortf.write(','.join((tup[0], tup[1], str(ts), tup[3])))
            sortf.write('\n')
    inf.close()
    sortf.close()
    print('sort by time')


def preprocess(sortfile, inputfile, delimeter):
    rowdict, coldict = {}, {}
    with open(sortfile, 'r') as sortf, open(inputfile, 'w') as outf:
        for line in sortf:
            usr, item, ts, num = line.strip().split(delimeter)
            if usr not in rowdict:
                rowdict[usr] = len(rowdict)
            map_row = rowdict[usr]
            col = item + ts
            if col not in coldict:
                coldict[col] = len(coldict)
            map_col = coldict[col]
            outline = delimeter.join((str(map_row), str(map_col), num, ts))
            outf.write(outline+'\n')
    sortf.close()
    outf.close()


def gen_hsfile(susp_infile, hsfile):
    'gen edgelist'
    dict = {}
    with open(susp_infile, 'r') as susf, open(hsfile, 'w') as hsf:
        for line in susf:
            item, user, num = line.strip().split(' ')
            key = item+'-'+user
            if key not in dict:
                dict[key] = int(num)
            else:
                dict[key] = dict[key] + int(num)
        tups = []
        for key in dict:
            value = dict[key]
            item, user = key.split('-')
            tup = (int(user), item, value)
            tups.append(tup)
        tups.sort(key=lambda x: x[0])
        'hs: user item num'
        for tup in tups:
            hsf.write(' '.join((str(tup[0]), tup[1], str(tup[2]))))
            hsf.write('\n')
    susf.close()
    hsf.close()


def gen_Fraudar(susp_infile, fraudar_file):
    dict = {}
    with open(susp_infile, 'r') as susf, open(fraudar_file, 'w') as fdf:
        for line in susf:
            item, user, num = line.strip().split(' ')
            key = item + '-' + user
            if key not in dict:
                dict[key] = int(num)
            else:
                dict[key] = dict[key] + int(num)
        tups = []
        for key in dict:
            value = dict[key]
            item, user = key.split('-')
            tup = (int(user), item, value)
            tups.append(tup)
        tups.sort(key=lambda x: x[0])
        'hs: user item num'
        for tup in tups:
            fdf.write(' '.join((str(tup[0]), tup[1], str(tup[2]))))
            fdf.write('\n')
    susf.close()
    fdf.close()

