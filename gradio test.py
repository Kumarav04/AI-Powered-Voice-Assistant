import gradio as gr

def record():
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


def image():
    img="UBC Fountain.jpg"

with gr.Blocks() as demo:
    btn = gr.Button("Start")
    output = gr.Image()
    btn.click(fn=image, outputs=output, api_name="image")
   

demo.launch()

    


















    
