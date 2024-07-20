import wave
import numpy as np
import sounddevice as sd
from scipy.signal import resample

def read_wav_file(filename):
    with wave.open(filename, 'rb') as wf:
        params = wf.getparams()
        frames = wf.readframes(params.nframes)
        signal = np.frombuffer(frames, dtype=np.int16)
        sample_rate = params.framerate
    return signal, sample_rate

def write_wav_file(filename, signal, sample_rate):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)  # 2 bytes for int16
        wf.setframerate(sample_rate)
        wf.writeframes(signal.tobytes())

def resample_signal(signal, original_rate, target_duration, original_duration):
    num_samples = int((target_duration / original_duration) * len(signal))
    resampled_signal = resample(signal, num_samples)
    return resampled_signal

def main():
    input_filename = './band_intro.wav'  # Cambia esto al nombre de tu archivo
    output_filename = 'output.wav'
    
    signal, sample_rate = read_wav_file(input_filename)
    original_duration = len(signal) / sample_rate
    target_duration = 10  # Nueva duración en segundos

    resampled_signal = resample_signal(signal, sample_rate, target_duration, original_duration)
    write_wav_file(output_filename, resampled_signal.astype(np.int16), sample_rate)

    print(f"Archivo procesado guardado como {output_filename}")

if __name__ == "__main__":
    main()
