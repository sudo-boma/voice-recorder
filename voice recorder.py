import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

freq = 44100
duration = 5

print("Recording started...")
recording = sd.rec(int(duration*freq), samplerate=freq, channels=2, dtype='float32')
sd.wait()

print("Recording stopped. Saving file...")
write("my_recording.wav", freq, recording)

print("Recording saved as 'my_recording.wav'")