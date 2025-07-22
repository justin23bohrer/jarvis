import sounddevice as sd
import vosk
import queue
import json
import os

# Queue to hold transcribed audio
q = queue.Queue()

# Path to your upgraded Vosk model
model_path = "vosk-model-en-us-0.22"

# Ensure the model directory exists
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model not found at: {model_path}")

# Load the high-accuracy model
model = vosk.Model(model_path)
rec = vosk.KaldiRecognizer(model, 16000)

# Audio callback: feeds audio data to Vosk recognizer
def callback(indata, frames, time, status):
    if rec.AcceptWaveform(bytes(indata)):
        result = json.loads(rec.Result())["text"]
        q.put(result)

# Main loop: listens for "jarvis", returns the command
def listen_for_jarvis_command():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("Say your command starting with 'jarvis'...")
        while True:
            phrase = q.get()
            if "jarvis" in phrase.lower():
                command = phrase.lower().split("jarvis", 1)[1].strip()
                print("Command detected:", command)
                return command
