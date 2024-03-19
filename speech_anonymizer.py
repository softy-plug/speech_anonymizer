import os

os.system("pip install sox")

import sox

import subprocess

# Get all audio files in the current directory
audio_files = [f for f in os.listdir('.') if f.endswith('.wav')]

# Loop through the audio files and apply voice anonymization
for audio_file in audio_files:
    # Create a new file name for the anonymized audio
    anon_file = audio_file.replace('.wav', '_anon.wav')

    # Apply voice anonymization using Sox
    subprocess.call(['sox', audio_file, anon_file, 'pitch -2'])

# softy_plug