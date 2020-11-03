class Matrix(object):
    def yielding(self, value):
        for i in range(1, value ** 2 + 1):
            yield i
    def make_matrix(self, value):
        a = self.yielding(value)
        return [[next(a) for i in range(value)] for i in range(value)]
    def printing_matrix(self, value=4):
        matrix = self.make_matrix(value)
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
mtr = Matrix()
mtr.printing_matrix(5)

