import numpy as np
from scipy.integrate import quad
from scipy.optimize import fsolve

def calcular_energia(tau):
    X_cuadrado = lambda omega: (tau * np.sinc(omega * tau / (2 * np.pi))) ** 2
    Energy, _ = quad(X_cuadrado, -1e-6, 1e-6)
    return Energy

def calcular_energia_y_banda_esencial():
    # Definir los valores de tau y beta
    tau = 1
    beta = 0.95

    # Calcular la energía total de la señal x(t) para tau dado
    E_total = calcular_energia(tau)

    # Definir la función X(omega)^2
    X_squared = lambda omega: (tau * np.sinc(omega * tau / (2 * np.pi))) ** 2

    # Definir la función de densidad espectral de energía normalizada
    X_squared_normalized = lambda omega: X_squared(omega) / E_total

    # Función para calcular la integral acumulada hasta una frecuencia omega
    def integral_acumulada(omega):
        if np.isscalar(omega):
            result, _ = quad(X_squared_normalized, -omega, omega)
        else:
            result = np.array([quad(X_squared_normalized, -w, w)[0] for w in omega])
        return result

    # Encontrar la banda esencial W tal que integral_acumulada(W) >= beta
    func = lambda omega: integral_acumulada(omega) - beta
    W = fsolve(func, [0, 100])[0]

    # Mostrar los resultados
    result = {
        'tau': tau,
        'energia_total': E_total,
        'banda_esencial_W': W
    }
    
    return result

# Ejecutar la función para calcular la energía y la banda esencial
resultado = calcular_energia_y_banda_esencial()
resultado