import numpy as np
import matplotlib.pyplot as plt

def espectro_frecuencia(tau, omega):
    X = tau * np.sinc(omega * tau / (2 * np.pi))
    return X

# Valores de tau para probar
taus = [1, 2, 0.5]

# Valores de omega
omega = np.linspace(-10, 10, 400)

plt.figure(figsize=(12, 8))

for tau in taus:
    X = espectro_frecuencia(tau, omega)
    plt.plot(omega, X, label=f'tau = {tau}')

plt.title('Espectro de Frecuencia')
plt.xlabel('Frecuencia (rad/s)')
plt.ylabel('Magnitud')
plt.legend()
plt.grid(True)
plt.show()
