import numpy as np
import matplotlib.pyplot as plt

# Генерируйте данные для графика (пример)
x = np.linspace(0, 1, 100)  # Создайте массив значений x
y = 1 / (1 + np.exp(-10 * (x - 0.5)))  # Пример функции логистической регрессии

# Создайте график
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="Логистическая регрессия")

# Настройте метки и заголовок
plt.xlabel("Признак")
plt.ylabel("Вероятность")
plt.title("График логистической регрессии")

# Добавьте легенду
plt.legend()

# Отобразите график
plt.show()