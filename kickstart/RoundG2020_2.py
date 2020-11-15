T = int(input())

for t in range(T):
    n = int(input())
    matrix = []
    best = 0

    for j in range(n):
        a = [int(x) for x in input().split()]
        matrix.append(a)

    #rows
    for i in range(n):
        current = 0
        for x in range(n-i):
            y = i + x
            current = current + matrix[x][y] 
        if current > best:
            best = current

    #columns
    for i in range(n):
        current = 0
        for x in range(n-i):
            y = i + x
            current = current + matrix[y][x]
        if current > best:
            best = current

    print("Case #" + str(t+1) + ": " + str(best))