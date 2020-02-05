import os
from processTensor import preprocess
from eigenpulse import slide_window

if __name__ == '__main__':
    path = '../data/beer'
    sortfile = os.path.join(path, 'sort.tensor')
    inputfile = os.path.join(path, 'input.tensor')
    preprocess(sortfile, inputfile, delimeter=',')

    outpath = '../output/beer'
    window, stride, l = 2, 1, 20
    slide_window(inputfile, outpath, window, stride, l)





