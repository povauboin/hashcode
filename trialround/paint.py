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
