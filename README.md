# voice-recorder
A minimal Python voice recorder that captures 5 seconds of stereo audio at 44.1kHz and saves it as "my_recording.wav". The script uses just three lines of core recording logic with sounddevice and scipy for audio capture and file output.
# Python Voice Recorder 

A minimal, functional voice recorder built with Python that captures audio and saves it as a WAV file.

## Features
- Records 5 seconds of stereo audio at CD quality (44.1kHz)
- Simple one-liner recording function
- Saves automatically as "my_recording.wav"
- Lightweight (under 15 lines of code)
- No dependencies beyond standard scientific Python libraries

## Installation

```bash
pip install sounddevice scipy numpy
```

## Usage

Run the script and it will automatically record for 5 seconds:

```bash
python recorder.py
```

Output:
```
Recording started...
Recording stopped. Saving file...
Recording saved as 'my_recording.wav'
```

## Code Overview

```python
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np

# Configuration
freq = 44100      # Sample rate (CD quality)
duration = 5      # Recording length in seconds

# Record audio
recording = sd.rec(int(duration*freq), samplerate=freq, channels=2, dtype='float32')
sd.wait()

# Save to file
write("my_recording.wav", freq, recording)
```

## Customization

Easily modify these variables:
- **`duration`**: Change recording time (in seconds)
- **`freq`**: Adjust sample rate (16000 for phone quality, 44100 for CD)
- **`channels`**: 1 for mono, 2 for stereo
- Filename in `write()` function

## Requirements
- Python 3.6+
- `sounddevice` (audio capture)
- `scipy` (WAV file writing)
- `numpy` (audio data handling)

## Limitations
- Fixed recording duration (cannot stop early)
- Overwrites "my_recording.wav" on each run
- No error handling for missing microphone
- No audio playback feature

## Perfect For
- Learning audio processing basics
- Quick voice memos
- Educational demonstrations
- As a starting point for more advanced recorders
