import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.fft import fft, fftfreq, ifft

# Definir el pulso unitario
def x_t(t, tau):
    return np.where(np.abs(t) <= tau / 2, 1, 0)

# Valores de tiempo
t = np.linspace(-3, 3, 1000)  # Aumentar el rango de tiempo para mejor visualización
tau = 1

# Graficar el pulso unitario
plt.plot(t, x_t(t, tau))
plt.title(f'Pulso unitario de duración τ={tau}')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.grid(True)
plt.show()

#===========Energia de la señal==================
# Calcular la energía de la señal
def energia_x_t(tau):
    integrando = lambda t: x_t(t, tau)**2
    energia, _ = quad(integrando, -tau/2, tau/2)
    return energia

# Calcular y mostrar la energía para τ=1
energia = energia_x_t(tau)
print(f'Energía de x(t) para τ={tau}: {energia}')

#========Probar con otros valores de τ=============
taus = [1.5, 2, 3]
for tau in taus:
    energia = energia_x_t(tau)
    print(f'Energía de x(t) para τ={tau}: {energia}')


#============Banda Esencial=========================
# Transformada de Fourier de la señal
def X_omega(t, tau):
    X_f = fft(x_t(t, tau))
    freqs = fftfreq(t.size, t[1] - t[0])
    return X_f, freqs

# Calcular la banda esencial
def banda_esencial(X_f, freqs, porcentaje=0.95):
    energia_total = np.sum(np.abs(X_f)**2)
    energia_acumulada = np.cumsum(np.abs(X_f)**2)
    idx = np.where(energia_acumulada >= porcentaje * energia_total)[0][0]
    banda = np.abs(freqs[idx])
    return banda

# Calcular y mostrar la banda esencial para τ=1
X_f, freqs = X_omega(t, tau)
banda = banda_esencial(X_f, freqs)
print(f'Banda esencial para τ={tau}: {banda}')


#===============Grafica Reconstruida==================
# Graficar la señal reconstruida a partir de la banda esencial
def señal_reconstruida(t, tau, banda):
    X_f, freqs = X_omega(t, tau)
    X_f[freqs > banda] = 0  # Filtrar frecuencias fuera de la banda esencial
    x_reconstruida = ifft(X_f)
    return np.real(x_reconstruida)

# Calcular y graficar la señal reconstruida 
x_rec = señal_reconstruida(t, tau, banda)
plt.plot(t, x_rec, label='Señal reconstruida')
plt.plot(t, x_t(t, tau), label='Señal original', linestyle='dashed')
plt.title('Señal reconstruida a partir de la banda esencial')
plt.xlabel('t')
plt.ylabel('x_hat(t)')
plt.legend()
plt.grid(True)
plt.show()
