#!/usr/bin/python
# -*- coding: utf-8 -*-


def ecriture(liste):
    fichier = open("fichier_res.txt","w")
    n = len(liste)
    liste.insert(0,str(n))
    res = ', '.join(liste)
    fichier.write(res)

    fichier.close()

def rapport(liste, S):
    N = len(liste)
    M = len(liste[0])
    n = (2*S+1)*(2*S+1)
    res = liste

    for i in xrange(N):
        for j in xrange(M):
            res[i][j] = (liste[i][j]*1.0)/n

    return res



test = [[0,1,2,2,2,1,0],[0,1,2,8,2,1,0],[0,1,2,2,2,1,0]]
print rapport(test,1)
