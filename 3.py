import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la señal
A1 = 1           # Amplitud de la señal
omega1 = 2 * np.pi * 5  # Frecuencia angular en radianes/segundo, ej. 5 Hz
t_max = 1        # Tiempo máximo de la simulación (en segundos)

# Función de la señal continua
def x_t(t):
    return A1 * np.sin(omega1 * t)


# Tiempo continuo para la señal
t_cont = np.linspace(0, t_max, 1000)
x_cont = x_t(t_cont)

# Escenario 1: Muestreo suficiente
Ts_suf = 1 / (10 * omega1 / (2 * np.pi))  # Ts = 1/(10*frecuencia)
t_suf = np.arange(0, t_max, Ts_suf)
x_suf = x_t(t_suf)

# Escenario 2: Muestreo ajustado
Ts_adj = 1 / (2 * omega1 / (2 * np.pi) + 0.1)  # Ts = 1/(2*frecuencia + 0.1)
t_adj = np.arange(0, t_max, Ts_adj)
x_adj = x_t(t_adj)

# Escenario 3: Muestreo insuficiente
Ts_insuf = 1 / (0.5 * omega1 / (2 * np.pi))  # Ts = 1/(0.5*frecuencia)
t_insuf = np.arange(0, t_max, Ts_insuf)
x_insuf = x_t(t_insuf)

plt.figure(figsize=(12, 8))

# Escenario 1: Muestreo suficiente
plt.subplot(3, 1, 1)
plt.plot(t_cont, x_cont, label='Señal Continua', color='blue')
plt.stem(t_suf, x_suf, linefmt='--', markerfmt='ro', basefmt='r-', label='Muestreo Suficiente')
plt.title('Muestreo Suficiente')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()

# Escenario 2: Muestreo ajustado
plt.subplot(3, 1, 2)
plt.plot(t_cont, x_cont, label='Señal Continua', color='blue')
plt.stem(t_adj, x_adj, linefmt='--', markerfmt='go', basefmt='g-', label='Muestreo Ajustado')
plt.title('Muestreo Ajustado')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()

# Escenario 3: Muestreo insuficiente
plt.subplot(3, 1, 3)
plt.plot(t_cont, x_cont, label='Señal Continua', color='blue')
plt.stem(t_insuf, x_insuf, linefmt='--', markerfmt='bo', basefmt='b-', label='Muestreo Insuficiente')
plt.title('Muestreo Insuficiente')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()

plt.tight_layout()
plt.show()
