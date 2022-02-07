# Дана прямоугольная таблица из 0 и 1. Необходимо занулить все строки и столбцы, в которых есть хотя бы один ноль.
# Формат ввода: в первой строке входных данных заданы целые числа n и m (1≤n, m≤1000)
# Следующие n строк содержат по m символов 0 или 1 - содержание таблицы.

n, m = map(int, input().split())
lines = []
for _ in range(n):
    line = []
    nn = str(input())
    for n in nn:
        line.append(int(n))
    lines.append(line)

x = []
y = []

for i in range(len(lines)):
    for j in range(m):
        if lines[i][j] == 0:
            x.append(i)
            y.append(j)

res = []
for i in range(len(lines)):
    if i in x:
        line = "0" * m
        res.append(line)
    else:
        line = []
        for j in range(m):
            if j in y:
                line.append("0")
            else:
                line.append('1')
        line = ''.join(line)
        res.append(line)
for re in res:
    print(re)