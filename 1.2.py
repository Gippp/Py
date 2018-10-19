n = int(input('n:'))
X = float(input('x:'))
Y = float(input('y:'))
# Скорость
x = 1/X
y = 1/Y
# Пропорции
x_p = x/(x+y)
y_p = 1 - x_p
# Распределение
x_n = int(n*x_p)
y_n = int(n*y_p)
# Остаток
n_n = n - x_n - y_n
# Ответ
answer = max(x_n/x, y_n/y) + (min(X,Y) if n_n else 0)
print(answer)
