#!/usr/bin/env python
# encoding: utf-8

def create_answer(V):

    f = open('answer.txt', 'w')
    f.write('%s\n' % len(V))
    for i in range(len(V)):
        f.write('%s\n' % len(V[i])) # nb intersections visitees par ci
        for edge in V[i]:
            f.write('%s\n' % edge) # depart

if '__main__' == __name__:

    C = 8
    S = 4516

    V = [[S, 4122, 7281, 2751] for i in range(C)]

    create_answer(V)
