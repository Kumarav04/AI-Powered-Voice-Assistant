import openai
import gradio as gr
from gtts import gTTS
import whisper as whisper
import numpy as np
import os
import pyaudio
import wave

def listen():
    global transcript
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 5
    filename = "output.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    with open("output.wav", "rb") as audio_file:
        transcript = openai.Audio.transcribe(
            file = audio_file,
            model = "whisper-1",
            response_format="text",
            language="en"
        )
    print(transcript)
    return transcript
        
def generate_response(myprompt):
    global answer
    api_key = "Enter your API Key here"
    openai.api_key = api_key
    response = openai.Completion.create(engine="text-davinci-002", prompt=myprompt, max_tokens=1000)
    answer = response.choices[0].text
    print(answer)
    return answer

def speak(mytext):
    audio= gTTS(text=mytext, lang = "en", slow=False)
    audio.save("answer.mp3")
    os.system("start answer.mp3")
    
listen()
      
