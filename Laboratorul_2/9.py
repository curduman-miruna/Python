def find_obstructed_seats(matrix):
    obstructed_seats = []
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(cols):
        for j in range(rows):
            height = matrix[j][i]
            for k in range(j - 1, -1, -1):
                if matrix[k][i] > height:
                    obstructed_seats.append((j, i))
                    break

    return obstructed_seats

stadium = [[1, 2, 3, 2, 1, 1],
           [2, 4, 4, 3, 7, 2],
           [5, 5, 2, 5, 6, 4],
           [6, 6, 7, 6, 7, 5]]

obstructed_seats = find_obstructed_seats(stadium)
print(obstructed_seats)
