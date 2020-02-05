import numpy as np
from scipy import sparse
from scipy.sparse.linalg import svds
import math


def generateA(xs, ys, data, index1, index2):
    row = xs[index1:index2]
    col = ys[index1:index2]
    data = data[index1: index2]
    m = max(row)+1
    n = max(col) +1
    mat = sparse.csr_matrix((data, (row, col)), shape=(m, n), dtype=np.int)
    return mat, n


def generateGH_by_multiply(A, Omg):
    G = A*Omg
    H = A.T*G
    return G, H


def generateGH_by_list(G, H, glist, hlist, k):
    if k == 0:
        for g in glist:
            G = np.vstack((G, g))
        for h in hlist:
            H = H + h
    else:
        g = glist.pop(0)
        gm = g.shape[0]
        G = G[gm:, :]
        h = hlist.pop(0)
        H = H - h
        G = np.vstack((G, glist[-1]))
        H = H + hlist[-1]
    return G, H, glist, hlist


def generateQB(G, H, Omg, k, b):
    m = G.shape[0]
    n = H.shape[0]
    l = k + 10
    Q = np.zeros((m, 0))
    B = np.zeros((0, n))
    t = int(math.floor(l/b))
    for i in range(0, t):
        temp = B * Omg[:, i*b: (i+1)*b]
        Yi = G[:, i*b: (i+1)*b] - Q*temp
        Qi, Ri = np.linalg.qr(Yi)
        Qi, Rit = np.linalg.qr(Qi - Q*(Q.T*Qi))
        Ri = Rit*Ri
        Bi = Ri.T.I * (H[:, i*b: (i+1)*b].T - Yi.T*Q*B - temp.T * B)
        Q = np.hstack((Q, Qi))
        B = np.vstack((B, Bi))
    return Q, B


def computeSVD(Q, B):
    u1, s, v = svds(B, 10, ncv=None, tol=0, which='LM',return_singular_vectors=True)
    u = Q * u1
    return u, s, v