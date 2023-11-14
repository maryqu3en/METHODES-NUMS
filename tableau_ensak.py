def fillMatrix(lines, columns):
    matrix = []
    for i in range(lines):
        row = []
        for j in range(columns):
            row.append(int(input("enter element ")))
        matrix.append(row)
    return matrix

def printMatrix(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end=" ")
        print()

def findMaxMin(matrix):
    min = matrix[0][0]
    max = matrix[0][0]
    for row in matrix:
        for elem in row:
            if elem < min:
                min = elem
            elif elem > max:
                max = elem
    return min, max

#main
line = int(input("Enter number of lines: "))
column = int(input("Enter number of columns: "))
matrix = fillMatrix(line, column)
printMatrix(matrix)

min, max = findMaxMin(matrix)

print("The min is: ",min)
print("the max is: ",max)