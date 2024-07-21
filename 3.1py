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

# Función para calcular el tiempo y señal muestreada
def tren_impulso_muestreos(factor, t_max):
    Ts = 1 / (factor * omega1 / (2 * np.pi))
    t_muestreo = np.arange(0, t_max, Ts)
    x_muestreo = x_t(t_muestreo)
    return t_muestreo, x_muestreo

# Escenarios de muestreo
factores = [10, 2 + 0.1/(omega1/(2 * np.pi)), 0.5]
muestreos = [tren_impulso_muestreos(f,t_max) for f in factores]

# Crear la figura y los subplots
fig, axs = plt.subplots(3, 2, figsize=(12, 10))

# Títulos y colores para los escenarios
titulos = ['Muestreo Suficiente', 'Muestreo Ajustado', 'Muestreo Insuficiente']
colores = ['ro', 'go', 'bo']

for i, (t_muestreo, x_muestreo) in enumerate(muestreos):
    # Graficar la señal muestreada
    axs[i, 1].plot(t_cont, x_cont, label='Señal Continua', color='blue')
    axs[i, 1].stem(t_muestreo, x_muestreo, linefmt='--', markerfmt=colores[i], basefmt='-', label=titulos[i])
    axs[i, 1].set_title(titulos[i])
    axs[i, 1].set_xlabel('Tiempo (s)')
    axs[i, 1].set_ylabel('Amplitud')
    axs[i, 1].legend(loc='lower right')

    # Graficar el tren de pulsos
    axs[i, 0].stem(t_muestreo, np.ones_like(t_muestreo), linefmt='--', markerfmt=colores[i], basefmt='-', label=f'Tren de Pulsos {titulos[i]}')
    axs[i, 0].set_title(f'Tren de Pulsos {titulos[i]}')
    axs[i, 0].set_xlabel('Tiempo (s)')
    axs[i, 0].set_ylabel('Amplitud')
    axs[i, 0].legend(loc='lower right')

plt.tight_layout()
plt.subplots_adjust(hspace=0.5)  # Aumentar el espacio vertical entre los gráficos
plt.show()




