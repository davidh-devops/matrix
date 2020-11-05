def order_canon(matrix):
    current_row = 0
    current_col = 0
    while current_row < len(matrix) and current_col < len(matrix[current_row]):
        if matrix[current_row][current_col] == 0:
            for m, inner_row in enumerate(matrix[current_row + 1:]):
                if inner_row[current_col] != 0:
                    temp_row = matrix[current_row]
                    matrix[current_row] = matrix[current_row + m + 1]
                    matrix[current_row + m + 1] = temp_row
        if matrix[current_row][current_col] != 1 and matrix[current_row][current_col] != 0:
            multiplyer = 1 / matrix[current_row][current_col]
            for n, inner_col in enumerate(matrix[current_row]):
                matrix[current_row][n] = multiplyer * inner_col
        for m, inner_row in enumerate(matrix[:current_row]):
            if matrix[current_row][current_col] != 0:
                multiplyer = -1 * inner_row[current_col] / matrix[current_row][current_col]
                for n, inner_col in enumerate(inner_row):
                    matrix[m][n] += multiplyer * matrix[current_row][n]
        for m, inner_row in enumerate(matrix[current_row + 1:]):
            if matrix[current_row][current_col] != 0:
                multiplyer = -1 * inner_row[current_col] / matrix[current_row][current_col]
                for n, inner_col in enumerate(inner_row):
                    matrix[current_row + 1 + m][n] += multiplyer * matrix[current_row][n]

        current_row += 1
        current_col += 1
    return matrix

matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
matrix = [[0, 0, 1],[0, 1, 0],[1, 0, 0]]
print(order_canon(matrix))