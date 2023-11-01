class Matrix:
    def __init__(self, n, m, data=None):
        self.n = n
        self.m = m
        if data is not None:
            if len(data) != n or any(len(row) != m for row in data):
                return "Data dimensions do not match specified dimensions (n, m)"
            self.elements = data
        else:
            self.elements = [[0 for _ in range(m)] for _ in range(n)]

    def set(self, row, col, value):
        if 0 <= row < self.n and 0 <= col < self.m:
            self.elements[row][col] = value
        else:
            return "Out of bound"

    def get(self, row, col):
        if 0 <= row < self.n and 0 <= col < self.m:
            return self.elements[row][col]
        else:
            return None

    def transpose(self):
        matrix = Matrix(self.m, self.n)
        for i in range(self.n):
            for j in range(self.m):
                matrix.set(j, i, self.get(i, j))
        return matrix

    def modify(self, transform):
        for i in range(self.n):
            for j in range(self.m):
                self.set(i, j, transform(self.get(i, j)))

    def matrix_multiply(self, other):
        # cij = aik*bkj , important ca ca m.self = n.other, self = a, other = b
        if self.m != other.n:
            raise ValueError("Matrix dimensions are not compatible for multiplication")

        result = Matrix(self.n, other.m) # = c
        for i in range(self.n):
            for j in range(other.m):
                c_ij = 0
                for k in range(self.m):
                    c_ij += self.elements[i][k] * other.elements[k][j]
                result.elements[i][j] = c_ij

        return result


matrix_data_1 = [
    [1, 2],
    [3, 4],
    [5, 6]
]

matrix_data_2 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix_1 = Matrix(3, 2, data=matrix_data_1)
matrix_2 = Matrix(2, 3, data=matrix_data_2)

print("Transposed matrix")
transposed = matrix_1.transpose()
for i in range(2):
    for j in range(3):
        print(transposed.get(i, j), end=" ")
    print()

result_matrix = matrix_1.matrix_multiply(matrix_2)
print("Multiplication Result:")
for i in range(3):
    for j in range(3):
        print(result_matrix.get(i, j), end=" ")
    print()

transform_func = lambda x: x + 2
matrix_1.modify(transform_func)

print("Tranformed matrix")
for i in range(3):
    for j in range(2):
        print(matrix_1.get(i, j), end=" ")
    print()