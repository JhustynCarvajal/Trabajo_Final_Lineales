Comandos Necesarios

1. Abrir y Leer Archivos de Audio WAV

    wave.open(filename, 'rb'): Abre un archivo WAV en modo lectura binaria.
        De dónde viene: Biblioteca estándar de Python wave.
        Uso: Permite acceder a la información del archivo de audio WAV.

    wf.getparams(): Obtiene los parámetros del archivo WAV, como la frecuencia de muestreo, número de canales, etc.
        De dónde viene: Método del objeto wave.Wave_read creado por wave.open().
        Uso: Recupera información esencial sobre el archivo de audio.

    wf.readframes(num_frames): Lee una cantidad específica de frames del archivo WAV.
        De dónde viene: Método del objeto wave.Wave_read.
        Uso: Extrae los datos de audio en bruto del archivo WAV.

    np.frombuffer(frames, dtype=np.int16): Convierte los datos de audio en bruto a una matriz de números enteros.
        De dónde viene: Función de la biblioteca numpy.
        Uso: Transforma los datos de audio en un formato que se puede manipular en Python.

2. Reproducir Audio

    sd.play(signal, samplerate=sample_rate): Reproduce una señal de audio.
        De dónde viene: Función de la biblioteca sounddevice.
        Uso: Permite reproducir el audio desde Python.

    sd.wait(): Espera a que termine la reproducción del audio.
        De dónde viene: Función de la biblioteca sounddevice.
        Uso: Sincroniza el código para que continúe solo después de que se haya terminado de reproducir el audio.

3. Manipular Señales de Audio

    resample(signal, num_samples): Redimensiona la señal a un nuevo número de muestras.
        De dónde viene: Función de la biblioteca scipy.signal.
        Uso: Cambia la frecuencia de muestreo de la señal, afectando su duración.

4. Visualizar la Señal de Audio

    plt.plot(time, signal): Grafica la señal de audio en función del tiempo.
        De dónde viene: Función de la biblioteca matplotlib.
        Uso: Permite visualizar la forma de onda del audio.

    plt.show(): Muestra la gráfica.
        De dónde viene: Función de la biblioteca matplotlib.
        Uso: Renderiza la gráfica en una ventana.

Análisis de Resultados:

    Visualización de la Señal de Audio:
    La gráfica que muestra la onda de audio ilustra claramente las características temporales de la señal. Esta representación es esencial para entender cómo se comporta la señal a lo largo del tiempo, permitiendo observar las variaciones en amplitud y frecuencia de manera visual. Este análisis es vital para captar la dinámica del audio, como los cambios en intensidad y ritmo.

    Impacto del Muestreo en la Calidad del Audio:
    Examinar la señal antes y después del muestreo proporciona una comprensión clara de cómo el proceso de muestreo influye en la calidad del sonido. Al utilizar una frecuencia de muestreo de 20000 Hz, que es algo exagerado pero sirve como ejeplo, se nota una significativa degradación en la calidad del audio. La señal resultante se torna menos clara y pierde muchos detalles en comparación con la señal original. Esto ocurre porque la reducción en la frecuencia de muestreo limita la cantidad de información que se captura, afectando la precisión y riqueza del sonido.

    Diferencias entre la Señal Original y la Señal Muestreada:
    La comparación entre la señal original y la señal muestreada revela las diferencias en calidad y fidelidad. La señal original conserva una mayor claridad y detalle en el sonido, mientras que la señal muestreada muestra una reducción en la fidelidad, con artefactos y distorsiones que afectan la percepción del audio. Esta comparación pone de relieve la importancia de seleccionar una frecuencia de muestreo adecuada para asegurar que se preserve la calidad del sonido y se minimice la pérdida de información durante el proceso de digitalización.