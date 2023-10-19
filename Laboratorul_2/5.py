def replace(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if i > j:
                matrix[i][j] = 0

    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result_matrix = replace(matrix)
for row in result_matrix:
    print(row)
