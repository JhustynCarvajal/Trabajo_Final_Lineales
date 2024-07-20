import wave
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.signal import resample
import tkinter as tk
from tkinter import filedialog

# Función para leer el archivo WAV
def read_wav_file(filename):
    with wave.open(filename, 'rb') as wf:
        params = wf.getparams()
        frames = wf.readframes(params.nframes)
        signal = np.frombuffer(frames, dtype=np.int16)
        sample_rate = params.framerate
    return signal, sample_rate

# Función para graficar la señal
def plot_signal(signal, sample_rate, title):
    duration = len(signal) / sample_rate
    time = np.linspace(0, duration, len(signal), endpoint=False)
    plt.figure(figsize=(10, 4))
    plt.plot(time, signal)
    plt.title(title)
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid()
    plt.show()

# Función para realizar el muestreo
def resample_signal(signal, original_rate, new_rate):
    num_samples = int(len(signal) * float(new_rate) / original_rate)
    resampled_signal = resample(signal, num_samples)
    return resampled_signal

# Función para graficar las señales original y muestreada
def plot_resampled_signal(original_signal, resampled_signal, original_rate, new_rate):
    duration_original = len(original_signal) / original_rate
    duration_resampled = len(resampled_signal) / new_rate
    
    time_original = np.linspace(0, duration_original, len(original_signal), endpoint=False)
    time_resampled = np.linspace(0, duration_resampled, len(resampled_signal), endpoint=False)

    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(time_original, original_signal, label='Original')
    plt.title('Señal Original')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid()

    plt.subplot(2, 1, 2)
    plt.plot(time_resampled, resampled_signal, label='Muestreada', color='r')
    plt.title('Señal Muestreada')
    plt.xlabel('Tiempo [s]')
    plt.ylabel('Amplitud')
    plt.grid()

    plt.tight_layout()
    plt.show()

# Función para reproducir audio
def play_audio(signal, sample_rate):
    sd.play(signal, samplerate=sample_rate)
    sd.wait()  # Esperar a que termine la reproducción

# Aplicación GUI con tkinter
class AudioProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Procesador de Audio")
        
        # Establecer el tamaño de la ventana
        self.root.geometry("400x100")  # Ancho x Alto
        
        self.filepath = None
        
        self.load_button = tk.Button(root, text="Cargar Archivo", command=self.load_file)
        self.load_button.pack(pady=10)
        
        self.sample_rate_label = tk.Label(root, text="Frecuencia de muestreo:")
        self.sample_rate_label.pack()
        
        self.sample_rate_entry = tk.Entry(root)
        self.sample_rate_entry.pack(pady=5)
        self.sample_rate_entry.insert(0, "22050")
        
        self.process_button = tk.Button(root, text="Procesar", command=self.process_audio)
        self.process_button.pack(pady=10)
        
    def load_file(self):
        self.filepath = filedialog.askopenfilename(filetypes=[("Archivos WAV", "*.wav")])
        if self.filepath:
            print(f"Archivo cargado: {self.filepath}")
    
    def process_audio(self):
        if self.filepath:
            signal, sample_rate = read_wav_file(self.filepath)
            new_rate = int(self.sample_rate_entry.get())
            resampled_signal = resample_signal(signal, sample_rate, new_rate)
            plot_resampled_signal(signal, resampled_signal, sample_rate, new_rate)
            
            print("Reproduciendo señal original...")
            play_audio(signal, sample_rate)
            
            print("Reproduciendo señal muestreada...")
            play_audio(resampled_signal, new_rate)
            
            print("Procesamiento completo.")
        else:
            print("No se ha cargado ningún archivo.")

# Ejecutar la aplicación GUI
root = tk.Tk()
app = AudioProcessorApp(root)
root.mainloop()
