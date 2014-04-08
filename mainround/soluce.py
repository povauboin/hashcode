#!/usr/bin/env python
# encoding: utf-8

import copy
from streetview import *
from goo import *
import random

def create_answer(V):

    f = open('answer.txt', 'w')
    f.write('%s\n' % len(V))
    for i in range(len(V)):
        f.write('%s\n' % len(V[i])) # nb intersections visitees par ci
        for edge in V[i]:
            f.write('%s\n' % edge) # depart

def look_ahead(s, cout, longueur, chemin, cost, score, depth):

    # print ('look_ahead, s: %s, depth: %s' % (s, depth))

    if depth <= 0:
        return (score, cost, chemin)

    J = 0
    best_score = score

    # longueur_copy = copy.deepcopy(longueur)

    for j in cout[s].keys():
        ratio = float(longueur[s][j]) / cout[s][j]

        longueur[s][j] /= 1.85
        if j in longueur and s in longueur[j]:
            longueur[j][s] /= 1.85

        (new_score, new_cost, new_path) = look_ahead(j, cout, longueur, chemin + [j], cost + [cout[s][j]], score + [ratio], depth-1)

        longueur[s][j] *= 1.85
        if j in longueur and s in longueur[j]:
            longueur[j][s] *= 1.85

        if sum(new_score) >= sum(best_score):
            J = j
            best_score = new_score
            best_path = new_path
            best_cost = new_cost

    return (best_score, best_cost, best_path)

def choix(s,cout,longueur, chemin, visited, classes, car_num):
    # n = len(cout[0])

    max_ratio = 0
    J = 0

    # choose next node only from neighbors in car sector
    neighbors = cout[s].keys()
    neighbors_in_sector = [node for node in neighbors if classes[node] == car_num]
    if False:
    # for j in neighbors_in_sector:
        ratio = float(longueur[s][j]) / cout[s][j]
        # if (not classes[j] == car_num):
        #     print ('increase ratio')
        #     ratio = 0
        ratios.append(ratio)
        # if longueur[s][j] == -1:
        #     continue
        if (ratio >= max_ratio):
            J = j
            max_ratio = ratio

    # if no neighbors is in sector
    look_ahead(s, cout, longueur, [], 0, 2)

    # print ('min ratio:', min(ratios))
    # print ('max ratio:', max(ratios))

    # if (cout[s][j] != -1):
    longueur[s][J] /= 1.85
    # if longueur[s][J] < 0:
    #     longueur[s][J] = 0
    if J in longueur and s in longueur[J]:
        longueur[J][s] /= 1.85

    return (J,cout[s][J],longueur, max_ratio)

# from http://stackoverflow.com/questions/4997851/python-dijkstra-algorithm
def dijkstra(net, s, t):
    print ('dijkstra')
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
    drop1 = copy.copy(labels) # used for looping
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
    temp = copy.copy(t)
    rpath = []
    path = []
    while 1:
        rpath.append(temp)
        if order.has_key(temp): temp = order[temp]
        else: return "There is no path from " + str(s) + " to " + str(t) + "."
        if temp == s:
            rpath.append(temp)
            break
    for j in range(len(rpath)-2,-1,-1):
        path.append(rpath[j])

    return path, labels[t]
    # return "The shortest path from " + s + " to " + t + " is " + str(path) + ". Minimum distance is " + str(labels[t]) + "."

# Given a large random network find the shortest path from '0' to '5'
# print dijkstra(net=randNet(), s='0', t='5')

# deplace une voiture de 1
def deplace1V(cout,longueur, S, T, first, visited, classes, car_num):

    chemin = [S]
    c = 0
    s = S

    steps = 0

    limit = 1
    loop = [False] * 10
    counter = 0

    path,t = dijkstra(cout, S, first)
    c += t
    for p in path:
        chemin.append(p)
        s = p

    while c <= T:
        (new_score, new_cost, new_path) = look_ahead(s, cout, longueur, [], [], [], 3)
        print (new_score, new_cost, new_path)
        for i in xrange(len(new_path)):
            # print ('add %s' % new_path[i])
            # print 'c', c
            # print ('len chemin %s' % len(chemin))
            longueur[s][new_path[i]] /= 1.85
            if new_path[i] in longueur and s in longueur[new_path[i]]:
                longueur[new_path[i]][s] /= 1.85
            c += new_cost[i]
            if c <= T:
                chemin.append(new_path[i])
                s = new_path[i]
            else:
                break

    print 'c', c
    print 'car_num', car_num
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

    visited = [0] * N

    # T = 3
    # S = 0

    classes = classer(coord, N)
    # print classes

    print 'choosing path'
    # chemin =  deplace1V(cost,length,S,T)
    # print chemin

    # C = 8
    # S = 4516

    # start = [1000, 250, 140, 4000, 5000, 152, 79, 8000]
    start = [264, 202, 975, 301, 1016, 1112, 992, 999]

    # V = [[S, 4122, 7281, 2751] for i in range(C)]
    V = []
    for i in range(C):
        (chemin,length) = deplace1V(cost,length,S,T, start[i], visited, classes, i+1)
        V.append(chemin)

    print 'writing answer'
    create_answer(V)
