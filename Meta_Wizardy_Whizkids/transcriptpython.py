# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 18:56:43 2024

@author: adity
"""

from google.cloud import speech_v1p1beta1 as speech
import os
import sys

def transcribe_audio(file_path, output_path):
    client = speech.SpeechClient()

    with open(file_path, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US'
    )

    response = client.recognize(config=config, audio=audio)

    transcript = ''
    for result in response.results:
        transcript += result.alternatives[0].transcript + '\n'

    with open(output_path, 'w') as output_file:
        output_file.write(transcript)

    return transcript

if __name__ == '__main__':
    if 'GOOGLE_APPLICATION_CREDENTIALS' not in os.environ:
        print("The Google Speech-to-Text API key is missing. Please set the GOOGLE_APPLICATION_CREDENTIALS environment variable.")
        sys.exit(1)
    
    file_path = sys.argv[1]
    output_path = sys.argv[2]
    print(transcribe_audio(file_path, output_path))
