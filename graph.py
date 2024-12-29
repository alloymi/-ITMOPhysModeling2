import numpy as np
from matplotlib import pyplot as plt
import main

# Константы
E_min = main.electric_field(main.U_min, main.r, main.R)
ay = (main.e * E_min) / main.m * np.ones(main.num_points)  # Постоянное ускорение
vy = ay * main.time  # Скорость как функция времени
y = 0.5 * ay * main.time ** 2  # Положение как функция времени
x = main.V0 * main.time  # Положение x на основе постоянной начальной скорости

# Построение графика
plt.figure(figsize=(10, 6))

# y(x)
plt.subplot(2, 2, 1)
plt.plot(x, y, label='y(x)')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('Траектория y(x)')
plt.legend()
plt.grid()

# Vy(t)
plt.subplot(2, 2, 2)
plt.plot(main.time, vy, label='Vy(t)', color='orange')
plt.xlabel('Время (s)')
plt.ylabel('Vy (m/s)')
plt.title('Скорость Vy(t)')
plt.legend()
plt.grid()

# ay(t)
plt.subplot(2, 2, 3)
plt.plot(main.time, ay, label='ay(t)', color='green')
plt.xlabel('Время (s)')
plt.ylabel('ay (m/s²)')
plt.title('Ускорение ay(t)')
plt.legend()
plt.grid()

# y(t)
plt.subplot(2, 2, 4)
plt.plot(main.time, y, label='y(t)', color='red')
plt.xlabel('Время (s)')
plt.ylabel('y (m)')
plt.title('Позиция y(t)')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
