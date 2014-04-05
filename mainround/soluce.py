#!/usr/bin/env python
# encoding: utf-8

def create_answer():

    C = 8
    S = 4516

    V = [[S] for i in range(C)]

    f = open('answer.txt', 'w')
    f.write('%s\n' % C)
    for i in range(C):
        f.write('%s\n' % len(V[i])) # nb intersections visitees par ci
        # f.write('%s\n' % S) # depart
        for edge in V[i]:
            f.write('%s\n' % edge) # depart

if '__main__' == __name__:

    create_answer()
