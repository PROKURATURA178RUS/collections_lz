n = 10  # Запишем любое значение, чтобы получить соответствующее количество элементов
fib_series = []

a, b = 0, 1 # Зададим переменные
count = 0

while count < n:     # Генерация ряда Фибоначчи
    fib_series.append(a)
    a, b = b, a + b
    count += 1


processed_series = []    # Обработка списка: четные элементы умножаются на 2, нечетные возводятся в квадрат
for num in fib_series:
    if num % 2 == 0:
        processed_series.append(num * 2)
    else:
        processed_series.append(num ** 2)


min_value = min(processed_series)    # Поиск минимального и максимального элементов
max_value = max(processed_series)
length = len(processed_series)


sorted_series = sorted(processed_series)     # Поиск медианного значения
median_index = length // 2
median_value = sorted_series[median_index] if length % 2 != 0 else (sorted_series[median_index - 1] + sorted_series[median_index]) / 2


median = sum(1 for x in processed_series if x > median_value)    # Подсчет элементов, больших медианного значения

# Вывод результатов
print("Ряд Фибоначчи:", fib_series)
print("Обработанный список:", processed_series)
print("Минимальный элемент:", min_value)
print("Максимальный элемент:", max_value)
print("Длина списка:", length)
print("Количество элементов больше медианного значения:", median)