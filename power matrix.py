#Программа возводит квадратную матрицу в k-ую степень
#На вход программе подаётся натуральное число 
#n — количество строк и столбцов в матрице, затем элементы матрицы, затем натуральное число k
#Программа выводит результирующую матрицу, разделяя элементы символом пробела.
n = int(input())
matrix1 = [[int(i) for i in input().split()] for _ in range(n)]
matrix2 = matrix1
k = int(input())-1
while k!=0:
    matrix = [[] for _ in range(n)]
    for z in range(n):
        for i in range(n):
            element = 0
            for j in range(n):
                element = element + matrix1[z][j]*matrix2[j][i]
            matrix[z].append(element)
    matrix1 = matrix
    k-=1
for i in range(n):
    for j in range(n):
        print(matrix[i][j],end = ' ')
    print()
#The program raises a square matrix to the kth power
#The input to the program is a natural number
#n is the number of rows and columns in the matrix, then the elements of the matrix, then the natural number k
#The program displays the resulting matrix, separating the elements with a space character.