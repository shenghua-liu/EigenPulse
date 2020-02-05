import numpy as np
import math


def filterEigenvec(A, u, v, k=0):
    m = A.shape[0]
    n = A.shape[1]
    num1 = 1 / math.sqrt(m)
    num2 = 1 / math.sqrt(n)
    list_u = u.tolist()
    list_v = v.tolist()
    list_i = [j for j, x in enumerate(list_u[k]) if abs(x) >= num1]
    list_j = [j for j, x in enumerate(list_v[k]) if abs(x) >= num2]
    B1 = A[list_i, :]
    B = B1[:, list_j]
    submat = B.todok()
    return submat


def calDensity(mat):
    num = np.sum(mat.data)
    density = round(float(num) / (mat.shape[0] + mat.shape[1]), 2)
    return density


def findSuspWins(densities):
    mean = np.mean(densities)
    std = np.std(densities, ddof=1)
    thres = 3*std + mean
    print 'mean:{}, std val:{}, thres:{}'.format(mean, std, thres)
    burst_wins = []
    for i in range(densities.__len__()):
        if densities[i] > thres:
            burst_wins.append(i)
    return burst_wins


def precision_recall_sets(trueset, predset):
    correct = 0
    for p in predset:
        if p in trueset: correct += 1
    precision = 0 if len(predset) == 0 else float(correct)/len(predset)
    recall = 0 if len(trueset)==0 else float(correct)/ len(trueset)
    return precision, recall


def calFmeasure(pre, rec):
    if pre+rec > 0:
	    f1 = 2*pre*rec/(pre+rec)
    else:
	    f1 = 0
    return f1


def gen_set(file):
    f = open(file, 'r')
    nums = set()
    for line in f.readlines():
        num = line.strip()
        nums.add(num)
    return nums