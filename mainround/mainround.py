#!/usr/bin/python
# -*- coding: utf-8 -*-


def choix(s,cout,longueur):
    n = len(cout[0])
    
    for j in xrange(n):
        if (cout[s][j] != 0):
            return (j,cout[s][j])


# décplace une voiture de 1
def deplace1V(cout,longueur, S, T):
    
    chemin = [S]
    c = 0
    s = S

    while c < T:
        (r,t) = choix(s,cout,longueur)
        chemin.append(r)
        c += t
        s = r

    return chemin


cout = [[0,1,0],
        [1,0,0],
        [1,1,0]]
longueur = [[0,1,0],
            [1,0,0],
            [1,1,0]]

T = 3
S = 0
chemin =  deplace1V(cout,longueur,S,T)
print chemin
