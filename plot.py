import numpy as np # Импорт numpy и matplotlib
import matplotlib.pyplot as plt

# Генерация данных
x = np.linspace(0, 2 * np.pi, 20)  # 20 точек от 0 до 2*pi
y =np.sin(x)   # Функция

# Создание графика
plt.figure(figsize=(10, 5))  # Задаем размер графика
plt.plot(x, y, marker='o', linestyle='-', color='b', label='y = sin(x)')  # Отрисовка линии с маркерами

# Настройка графика
plt.title('График функции y = sin(x)')  # Заголовок
plt.xlabel('x')  # Метка оси x
plt.ylabel('y')  # Метка оси y


plt.show()# Показать график