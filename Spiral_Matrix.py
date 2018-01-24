matrix=[[ 1, 2, 3, 4, 5, 6, 7, 8, 9],[ 11, 12, 13, 14, 15, 16, 17, 18, 19],[ 21, 22, 23, 24, 25, 26, 27, 28, 29],[ 31, 32, 33, 34, 35, 36, 37, 38, 39]]
ret = []

while matrix:
    ret += matrix.pop(0)
    if matrix and matrix[0]:
        for row in matrix:
            ret.append(row.pop())
    if matrix:
        ret += matrix.pop()[::-1]
    if matrix and matrix[0]:
        for row in matrix[::-1]:
            ret.append(row.pop(0))
print(ret)

# print(zip(*matrix)[::-1])
# #
# def spiralOrder(matrix):
#     return matrix and list(matrix.pop(0)) + spiralOrder(zip(*matrix)[::-1])
# # print(zip(*matrix)[::-1])
# print(spiralOrder(matrix))