import wave
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import resample
import sounddevice as sd
import tkinter as tk
from tkinter import filedialog

# Función para leer el archivo WAV
def read_wav_file(filename):
    # Abre el archivo WAV en modo lectura binaria
    with wave.open(filename, 'rb') as wf:
        # Obtiene los parámetros del archivo (número de canales, tasa de muestreo, etc.)
        params = wf.getparams()
        # Lee todos los fotogramas del archivo
        frames = wf.readframes(params.nframes)
        # Convierte los fotogramas en una matriz numpy de enteros de 16 bits
        signal = np.frombuffer(frames, dtype=np.int16)
        # Obtiene la tasa de muestreo del archivo
        sample_rate = params.framerate
    # Retorna la señal y la tasa de muestreo
    return signal, sample_rate

# Función para graficar la señal
def plot_signal(signal, sample_rate, title):
    # Calcula la duración de la señal en segundos
    duration = len(signal) / sample_rate
    # Crea un vector de tiempo basado en la duración y la cantidad de muestras
    time = np.linspace(0, duration, len(signal), endpoint=False)
    # Configura el tamaño de la figura del gráfico
    plt.figure(figsize=(10, 4))
    # Grafica la señal en función del tiempo
    plt.plot(time, signal)
    # Añade el título al gráfico
    plt.title(title)
    # Añade la etiqueta al eje x
    plt.xlabel('Tiempo [s]')
    # Añade la etiqueta al eje y
    plt.ylabel('Amplitud')
    # Añade una cuadrícula al gráfico
    plt.grid()
    # Muestra el gráfico
    plt.show()

# Función para realizar el muestreo
def resample_signal(signal, original_rate, new_rate):
    # Calcula el número de muestras en la nueva tasa de muestreo
    num_samples = int(len(signal) * float(new_rate) / original_rate)
    # Realiza el remuestreo de la señal
    resampled_signal = resample(signal, num_samples)
    # Retorna la señal remuestreada
    return resampled_signal

# Función para graficar las señales original y muestreada
def plot_resampled_signal(original_signal, resampled_signal, original_rate, new_rate):
    # Calcula la duración de la señal original en segundos
    duration_original = len(original_signal) / original_rate
    # Calcula la duración de la señal remuestreada en segundos
    duration_resampled = len(resampled_signal) / new_rate
    
    # Crea un vector de tiempo para la señal original
    time_original = np.linspace(0, duration_original, len(original_signal), endpoint=False)
    # Crea un vector de tiempo para la señal remuestreada
    time_resampled = np.linspace(0, duration_resampled, len(resampled_signal), endpoint=False)

    # Configura el tamaño de la figura del gráfico
    plt.figure(figsize=(12, 6))

    # Gráfica de la señal original
    plt.subplot(2, 1, 1)
    plt.plot(time_original, original_signal, label='Original')
    plt.title('Señal Original')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid()

    # Gráfica de la señal remuestreada
    plt.subplot(2, 1, 2)
    plt.plot(time_resampled, resampled_signal, label='Muestreada', color='r')
    plt.title('Señal Muestreada')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid()

    # Ajusta el diseño del gráfico para que no haya solapamientos
    plt.tight_layout()
    # Muestra el gráfico
    plt.show()

# Función para reproducir audio
def play_audio(signal, sample_rate):
    # Reproduce la señal de audio a la tasa de muestreo especificada
    sd.play(signal, samplerate=sample_rate)
    # Espera a que termine la reproducción
    sd.wait()

# Aplicación GUI con tkinter
class AudioProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Procesador de Audio")
        
        # Establecer el tamaño de la ventana
        self.root.geometry("400x150")  # Ancho x Alto
        
        self.filepath = None
        
        # Botón para cargar archivo
        self.load_button = tk.Button(root, text="Cargar Archivo", command=self.load_file)
        self.load_button.pack(pady=10)
        
        # Etiqueta para la frecuencia de muestreo
        self.sample_rate_label = tk.Label(root, text="Frecuencia de muestreo:")
        self.sample_rate_label.pack()
        
        # Entrada para la frecuencia de muestreo
        self.sample_rate_entry = tk.Entry(root)
        self.sample_rate_entry.pack(pady=5)
        self.sample_rate_entry.insert(0, "22050")  # Valor predeterminado
        
        # Botón para procesar el audio
        self.process_button = tk.Button(root, text="Procesar", command=self.process_audio)
        self.process_button.pack(pady=10)
        
    def load_file(self):
        # Diálogo para seleccionar un archivo WAV
        self.filepath = filedialog.askopenfilename(filetypes=[("Archivos WAV", "*.wav")])
        if self.filepath:
            print(f"Archivo cargado: {self.filepath}")
    
    def process_audio(self):
        if self.filepath:
            # Leer el archivo WAV
            signal, sample_rate = read_wav_file(self.filepath)
            # Obtener la nueva tasa de muestreo de la entrada
            new_rate = int(self.sample_rate_entry.get())
            # Realizar el remuestreo de la señal
            resampled_signal = resample_signal(signal, sample_rate, new_rate)
            # Graficar las señales original y remuestreada
            plot_resampled_signal(signal, resampled_signal, sample_rate, new_rate)
            
            # Reproducir la señal original
            print("Reproduciendo señal original...")
            play_audio(signal, sample_rate)
            
            # Reproducir la señal remuestreada
            print("Reproduciendo señal muestreada...")
            play_audio(resampled_signal, new_rate)
            
            print("Procesamiento completo.")
        else:
            print("No se ha cargado ningún archivo.")

# Ejecutar la aplicación GUI
root = tk.Tk()
app = AudioProcessorApp(root)
root.mainloop()