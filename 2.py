import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.fft import ifft, fftshift

def fsinc(x):
    """Función sinc normalizada."""
    return np.sinc(x / np.pi)

def calcular_banda_esencial(tau, beta, tol):
    """
    Calcular la banda esencial que contiene beta% de la energía total de la señal.

    Args:
        tau (float): Parámetro de la función sinc.
        beta (float): Proporción de la energía total que queremos contener (entre 0 y 1).
        tol (float): Tolerancia para la convergencia del cálculo.

    Returns:
        tuple: (W, energia_W) donde W es la banda esencial y energia_W es la energía en la banda W.
    """
    # Definir la función sinc
    f_sinc = lambda x: np.sinc(x / np.pi)

    # Definimos la función de la transformada de Fourier
    f = lambda omega, tau: tau * f_sinc(omega * tau / 2)

    # Definir la función X_cuadrada
    X_cuadrada = lambda omega, tau: np.real(np.abs(f(omega, tau)) ** 2)

    # Calcular la energía total de x(t)
    E = beta * tau

    # Inicializar variables
    W = 0
    step = 2 * np.pi / tau
    relerr = np.inf  # Inicializar con un valor grande

    # Iteración para encontrar la banda esencial
    while abs(relerr) > tol:
        # Calcular la energía en la banda W
        energia_W, _ = quad(lambda omega: X_cuadrada(omega, tau) / (2 * np.pi), -W, W)

        # Actualizar el error relativo
        relerr = (E - energia_W) / E

        # Ajustar W y step según el error relativo
        if relerr > 0:
            W += step
        else:
            step /= 2
            W -= step

    return W, energia_W

def calcular_energia(tau):
    """
    Calcular la energía total de la señal x(t) para un valor dado de tau.

    Args:
        tau (float): Parámetro de la función sinc.

    Returns:
        float: Energía total de la señal.
    """
    X_cuadrado = lambda omega: (tau * fsinc(omega * tau / 2)) ** 2
    Energy, _ = quad(X_cuadrado, -800, 800)
    return Energy

# Parámetros de prueba
tau = 1
beta = 0.95
tol = 1e-6

# Calcular la banda esencial
W, energia_W = calcular_banda_esencial(tau, beta, tol)
print(f'Banda esencial que contiene el {beta * 100:.2f}% de la energía para tau = {tau} es {W:.4f} rad/s')

# Graficar la señal x(t) reconstruida usando la banda esencial encontrada
omega = np.linspace(-4 * np.pi, 4 * np.pi, 200)
X = lambda omega: tau * fsinc(omega * tau / 2)

# Reconstruir la señal en el tiempo usando la transformada inversa de Fourier
t = np.linspace(-10, 10, 1000)
x_reconstruida = np.zeros_like(t)
for i in range(len(t)):
    integrand = lambda omega: np.real(X(omega) * np.exp(1j * omega * t[i]))
    x_reconstruida[i], _ = quad(integrand, -W, W)

# Graficar la señal reconstruida
plt.figure(figsize=(12, 6))
plt.plot(t, x_reconstruida, 'b', linewidth=2)
plt.grid(True)
plt.xlabel('Tiempo (t)')
plt.ylabel('x(t)')
plt.title('Señal reconstruida a partir de la banda esencial')
plt.show()

# Prueba de cálculo de energía para diferentes valores de tau
tau_valores = [2, 3, 5]
for tau in tau_valores:
    energia = calcular_energia(tau)
    print(f'Energía de la señal para tau = {tau} es {energia:.4f}')