import numpy as np
import matplotlib.pyplot as plt

def espectro_frecuencia(taus,omega):
    
    plt.figure(figsize=(6, 5))

    for tau in taus:
        X = tau * np.sinc(omega * tau / 2)
        plt.plot(omega, X, label=f'tau = {tau}')

    plt.title('Espectro de Frecuencia')
    plt.xlabel('Frecuencia (rad/s)')
    plt.ylabel('Magnitud')
    plt.legend()
    plt.grid(True)
    plt.show()

# Valores de omega
omega = np.linspace(-15, 15, 1000)

#Valores para tau
taus = [1, 2, 0.5]
    
espectro_frecuencia(taus, omega)