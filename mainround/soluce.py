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
    longueur[s][J] /= 2
    if longueur[s][J] < 0:
        longueur[s][J] = 0

    return (J,cout[s][J],longueur)

# from http://stackoverflow.com/questions/4997851/python-dijkstra-algorithm
def dijkstra(net, s, t):
    # sanity check
    if s == t:
        return "The start and terminal nodes are the same. Minimum distance is 0."
    if net.has_key(s)==False:
        return "There is no start node called " + str(s) + "."
    if net.has_key(t)==False:
        return "There is no terminal node called " + str(t) + "."
    # create a labels dictionary
    labels={}
    # record whether a label was updated
    order={}
    # populate an initial labels dictionary
    for i in net.keys():
        if i == s: labels[i] = 0 # shortest distance form s to s is 0
        else: labels[i] = float("inf") # initial labels are infinity
    from copy import copy
    drop1 = copy(labels) # used for looping
    ## begin algorithm
    while len(drop1) > 0:
        # find the key with the lowest label
        minNode = min(drop1, key = drop1.get) #minNode is the node with the smallest label
        # update labels for nodes that are connected to minNode
        for i in net[minNode]:
            if labels[i] > (labels[minNode] + net[minNode][i]):
                labels[i] = labels[minNode] + net[minNode][i]
                drop1[i] = labels[minNode] + net[minNode][i]
                order[i] = minNode
        del drop1[minNode] # once a node has been visited, it's excluded from drop1
    ## end algorithm
    # print shortest path
    temp = copy(t)
    rpath = []
    path = []
    while 1:
        rpath.append(temp)
        if order.has_key(temp): temp = order[temp]
        else: return "There is no path from " + str(s) + " to " + str(t) + "."
        if temp == s:
            rpath.append(temp)
            break
    for j in range(len(rpath)-1,-1,-1):
        path.append(rpath[j])

    return path, labels[t]
    # return "The shortest path from " + s + " to " + t + " is " + str(path) + ". Minimum distance is " + str(labels[t]) + "."

# Given a large random network find the shortest path from '0' to '5'
# print dijkstra(net=randNet(), s='0', t='5')

# deplace une voiture de 1
def deplace1V(cout,longueur, S, T, first):

    chemin = []
    c = 0
    s = S

    steps = 0

    path,t = dijkstra(cout, S, first)
    c += t
    for p in path:
        chemin.append(p)
        s = p

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

    start = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000]

    # V = [[S, 4122, 7281, 2751] for i in range(C)]
    V = []
    for i in range(C):
        (chemin,length) = deplace1V(cost,length,S,T, start[i])
        V.append(chemin)

    print 'writing answer'
    create_answer(V)
