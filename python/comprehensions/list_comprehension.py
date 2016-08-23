print range(10)
print [x + 1 for x in range(10)]
print [x ** 2 for x in range(10) if x % 2 == 0]
print [x + y for x in 'ABC' for y in '123']
print [x + y for x in 'ABC' if x != 'B' for y in '123' if y != '2']

#you can do matrix operations too like matrix multiplication..
#assumes 2 2-dimensional matrices having the same number of rows and columns
matrix1 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
matrix2 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print [[matrix1[row][col] * matrix2[row][col] for col in range(len(matrix1[0]))] for row in range(len(matrix1))]