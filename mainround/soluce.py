#!/usr/bin/env python
# encoding: utf-8

from streetview import *

def create_answer(V):

    f = open('answer.txt', 'w')
    f.write('%s\n' % len(V))
    for i in range(len(V)):
        f.write('%s\n' % len(V[i])) # nb intersections visitees par ci
        for edge in V[i]:
            f.write('%s\n' % edge) # depart

def choix(s,cout,longueur):
    # n = len(cout[0])

    max = 0
    J = 0
    # for j in xrange(n):
    for j in cout[s].keys():
        ratio = float(longueur[s][j]) / cout[s][j]
        # if longueur[s][j] == -1:
        #     continue
        if ratio >= max:
            J = j
            max = ratio

    # if (cout[s][j] != -1):
    longueur[s][J] -= 10
    if longueur[s][J] < 0:
        longueur[s][J] = 0

    return (J,cout[s][J],longueur)


# deplace une voiture de 1
def deplace1V(cout,longueur, S, T):

    chemin = [S]
    c = 0
    s = S

    steps = 0

    while c < T:
        (r,t,longueur) = choix(s,cout,longueur)
        if (c + t) <= T:
            chemin.append(r)
            s = r
        c += t
        # steps += 1
        # if steps >= 500:
        #     break

    print 'c', c
    return (chemin,longueur)

if '__main__' == __name__:

    # cout = [[0,1,0],
    #         [1,0,0],
    #         [1,1,0]]
    # longueur = [[0,1,0],
    #             [1,0,0],
    #             [1,1,0]]

    print 'reading map'
    N, M, T, C, S, coord, cost, length = readfile('paris_54000.txt')

    print 'N, M, T, C, S'
    print N, M, T, C, S

    # T = 3
    # S = 0

    print 'choosing path'
    # chemin =  deplace1V(cost,length,S,T)
    # print chemin

    # C = 8
    # S = 4516

    # V = [[S, 4122, 7281, 2751] for i in range(C)]
    V = []
    for i in range(C):
        (chemin,length) = deplace1V(cost,length,S,T)
        V.append(chemin)

    print 'writing answer'
    create_answer(V)
