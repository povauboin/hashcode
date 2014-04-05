def readfile(filename):
    data = open(filename)
    line1 = data.readline()
    N, M, T, C, S = map(int, line1.rstrip('\n').split(' '))
    
    coord = []
    for k in range(N):
        line = data.readline()
        (x, y) = tuple(map(float, line.rstrip('\n').split(' ')))
        coord.append((x, y))
    
    cost = [[-1 for j in range(N)] for i in range(N)]
    length = [[-1 for j in range(N)] for i in range(N)]
    for k in range(M):
        line = data.readline()
        i, j, ways, streetcost, streetlength = map(int, line.rstrip('\n').split(' '))
        cost[i][j], length[i][j] = streetcost, streetlength
        if ways == 2:
            cost[j][i], length[j][i] = streetcost, streetlength        
    
    return N, M, T, C, S, coord, cost, length
