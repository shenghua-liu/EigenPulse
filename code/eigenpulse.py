import numpy as np
from numpy import random
import SinglePassPCA
import processTensor
import util
import os


def slide_window(inputfile, outpath, window, stride, l):
    xs, ys, nums, tslist = processTensor.readfile(inputfile)
    ts_idx_tuple_list = []
    ts_idx_tuple_list.append((tslist[0], 0))
    densities = []
    length = xs.__len__()
    window_idx = 0
    for i in range(1, length):
        ts = tslist[i]
        if ts - ts_idx_tuple_list[-1][0] >= stride:
            ts_idx_tuple_list.append((ts, i))
            if ts - ts_idx_tuple_list[0][0] >= window:
                start_ts_row = ts_idx_tuple_list[0][1]
                mat = SinglePassPCA.generateA(xs, ys, nums, start_ts_row, i)
                n = max(ys[start_ts_row: i]) + 1
                Omg = np.mat(random.randn(n, l), dtype=np.float16)
                G, H = SinglePassPCA.generateGH_by_multiply(mat, Omg)
                Q, B = SinglePassPCA.generateQB(G, H, Omg, 10, 5)
                u1, s1, v1 = SinglePassPCA.computeSVD(Q, B)
                u1 = u1.T
                submat = util.filterEigenvec(mat, u1, v1)
                submatfile = os.path.join(outpath, 'window_%d_mat.npy' % window_idx)
                np.save(submatfile, submat)
                window_idx += 1

                density = util.calDensity(submat)
                densities.append(density)
                ts_idx_tuple_list.pop(0)
    susp_wins = util.findSuspWins(densities)
    print('suspicious windows:', susp_wins)









