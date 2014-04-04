#!/usr/bin/env python
# encoding: utf-8

matrix = [
    [1, 0, 1, 1],
    [0, 1, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
]

def readfile(filename):
    input = open(filename)
    line1 = input.readline()
    n, m = map(int, line1.rstrip('\n').split(' '))
    matrix = []
    for i in range(n):
        line = input.readline()
        matrix.append(map(int, line.replace('#','1 ').replace('.','0 ').rstrip(' \n').split(' ')))
    input.close()
    return (n, m, matrix)

def score_neighbors(matrix, S):

    N = len(matrix)
    M = len(matrix[0])

    scores = []

    for i in xrange(N):
        scores.append([])
        for j in xrange(M):
            scores[i].append(0)

    for i in xrange(S, N-S):
        for j in xrange(S, M-S):

            score = 0
            for x in xrange(i-S,i+S+1):
                for y in xrange(j-S,j+S+1):
                    # print (x, y, matrix[x][y])
                    score += matrix[x][y]

            scores[i][j] = score

    return scores

def print_command(matrix):
    N = len(matrix)
    M = len(matrix[0])

    commands = []
    for i in xrange(N):
        for j in xrange(M):

            if matrix[i][j] == 1:
                commands.append('PAINTSQ %s %s 0' % (i, j))

    return commands

def ecriture(liste):
    fichier = open("fichier_res.txt","w")
    n = len(liste)
    liste.insert(0,str(n))
    res = '\n'.join(liste)
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

if __name__ == '__main__':
    (n, m, matrix) = readfile('doodle.txt')
    # print n, m
    # scores = score_neighbors(matrix, 0)
    commands = print_command(matrix)
    # print scores

    ecriture(commands)

    # f = open('answer.txt', 'w')
    # f.write(str(len(commands)) + '\n')
    # f.write('\n'.join(commands))
    # f.close()
