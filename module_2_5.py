def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        str_matrix = []
        for j in range(m):
            str_matrix.append(value)
        matrix.append(str_matrix)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)

# Другой вариант:

n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
value = int(input('Введите желаемое значение: '))


def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        str_matrix = []
        for j in range(m):
            str_matrix.append(value)
        matrix.append(str_matrix)
    return matrix


matrix = get_matrix(n, m, value)

for str_matrix in matrix:
    print(*str_matrix)
