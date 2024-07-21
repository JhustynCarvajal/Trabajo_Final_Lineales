import numpy as np
import matplotlib.pyplot as plt

# Función para generar tren de impulsos con ZOH
def retenedor_ZOH(A1, omega1, t, Ts):
    # Generar puntos de muestreo en el intervalo de la señal original
    t_min = t[0]
    t_max = t[-1]
    t_muestreo = np.arange(t_min, t_max, Ts)
    x_muestreo = A1 * np.sin(omega1 * t_muestreo)

    # Inicializar la señal muestreada
    x_muestreada = np.zeros_like(t)

    # Aplicar muestreo con ZOH
    idx_muestreo = 0
    for i in range(len(t)):
        if t[i] >= t_muestreo[idx_muestreo]:
            x_muestreada[i] = x_muestreo[idx_muestreo]
            idx_muestreo += 1
            if idx_muestreo >= len(t_muestreo):
                break
        else:
            x_muestreada[i] = x_muestreo[idx_muestreo - 1]
    
    return x_muestreada

# Parámetros de la señal sinusoidal
A1 = 1
ω1 = 2 * np.pi * 5  # Frecuencia angular en radianes por segundo
t = np.linspace(0, 1, 1000)  # Tiempo de 0 a 1 segundo

# Crear la señal sinusoidal
x_t = A1 * np.sin(ω1 * t)

# Periodos de muestreo para los diferentes escenarios
T_s_suf = 0.05  # Muestreo suficiente (menor o igual a T1 / 2)
T_s_ajust = 0.0255  # Muestreo ajustado (algo mayor que T1 / 2)
T_s_insuf = 0.4  # Muestreo insuficiente (mayor que T1 / 2)

# Aplicar ZOH a los tres escenarios
x_t_suf_zoh = retenedor_ZOH(A1, ω1, t, T_s_suf)
x_t_ajust_zoh = retenedor_ZOH(A1, ω1, t, T_s_ajust)
x_t_insuf_zoh = retenedor_ZOH(A1, ω1, t, T_s_insuf)

# Graficar resultados del ZOH
plt.figure(figsize=(12, 8))

# Retenedor de orden cero (ZOH) para muestreo suficiente
plt.subplot(3, 1, 1)
plt.grid(True)
plt.plot(t, x_t, label='Señal Sinusoidal', alpha=0.5)
plt.step(t, x_t_suf_zoh, where='post', label='ZOH Muestreo Suficiente', color='orange')
plt.title('ZOH - Muestreo Suficiente')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()

# Retenedor de orden cero (ZOH) para muestreo ajustado
plt.subplot(3, 1, 2)
plt.grid(True)
plt.plot(t, x_t, label='Señal Sinusoidal', alpha=0.5)
plt.step(t, x_t_ajust_zoh, where='post', label='ZOH Muestreo Ajustado', color='orange')
plt.title('ZOH - Muestreo Ajustado')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()

# Retenedor de orden cero (ZOH) para muestreo insuficiente
plt.subplot(3, 1, 3)
plt.grid(True)
plt.plot(t, x_t, label='Señal Sinusoidal', alpha=0.5)
plt.step(t, x_t_insuf_zoh, where='post', label='ZOH Muestreo Insuficiente', color='orange')
plt.title('ZOH - Muestreo Insuficiente')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.legend()

plt.tight_layout()
plt.show()
