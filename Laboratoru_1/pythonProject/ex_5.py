def spiral_order(matrix):
    if not matrix:
        return []

    top = left = 0
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1

    result = []

    while True:
        if left > right:
            break

        # ->
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        if top > bottom:
            break

        # in jos
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if left > right:
            break

        # <-
        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

        if top > bottom:
            break

        # in sus
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

    return result


# Test the function
matrix = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['a', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']
]

print(''.join(spiral_order(matrix)))
