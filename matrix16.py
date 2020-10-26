matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

i = 0
n = len(matrix)
while i < n:
    n = len(matrix)
    if n != 0:
        if matrix[i] is matrix[-1]:
            for _ in matrix[i]:
                print(_)
            del matrix[i]
            i = n - 2
            while i >= 0:
                print(matrix[i][-1])
                del matrix[i][-1]
                i -= 1
            if len(matrix) != 0:
                i = len(matrix[0]) - 1
                while i >= 0:
                    print(matrix[0][i])
                    i -= 1
                del matrix[0]
                i = 0
        else:
            print(matrix[i][0])
            del matrix[i][0]
            i += 1
    else:
        break
