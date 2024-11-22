import numpy as np # Импорт numpy


identity_matrix_fib = np.eye(5)# Создание единичной матрицы размером 5x5
identity_matrix_ber = np.eye(5)


fib_sequence = [0, 1] # Генерация первых 5 чисел Фибоначчи
for i in range(2, 5):
    fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

# Генерация первых 5 чисел Бернулли (B_n = 1/n! * SUM(k=0 to n)(C(n, k) * B_k) для n >= 0)
bernoulli_sequence = [1, -0.5, 0.16666666667, 0, 0.04166666667]  # Первые 5 чисел ряда Бернулли


fib_matrix = np.tile(fib_sequence, (5, 1))# Создание матриц Фибоначчи и Бернулли размером 5x5
bernoulli_matrix = np.tile(bernoulli_sequence, (5, 1))


result_matrix_fib = identity_matrix_fib + fib_matrix   # Сложение единичных матриц с матрицами Фибоначчи и Бернулли
result_matrix_ber = identity_matrix_ber + bernoulli_matrix
result = result_matrix_fib * result_matrix_ber


print("Единичная матрица (5x5) для Фибоначчи:")# Вывод результатов
print(identity_matrix_fib)
print("Матрица Фибоначчи (5x5):")
print(fib_matrix)
print("Результат сложения с рядом Фибоначчи:")
print(result_matrix_fib)

print("Единичная матрица (5x5) для Бернулли:")
print(identity_matrix_ber)
print("Матрица Бернулли (5x5):")
print(bernoulli_matrix)
print("Результат сложения с рядом Бернулли:")
print(result_matrix_ber)

print("Результат Фибоначчи и Бернулли:")
print(result)

print('Полученная матрица меньше данной в условии')