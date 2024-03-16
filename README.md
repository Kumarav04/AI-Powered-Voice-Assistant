# AI Powered Voice Assistant

**Overview:**
This project utilizes various technologies to create a voice-driven AI assistant capable of understanding spoken language, generating responses, and converting text to speech for communication. The assistant interacts with users through voice input and output, providing a seamless conversational experience.

**Features:**
1. **Speech Recognition:** The chatbot can transcribe spoken words into text using OpenAI's Whisper API, enabling users to communicate with the system via voice input.
   
2. **AI Response Generation:** It leverages OpenAI's powerful language models to generate responses to user queries or prompts. The AI model understands natural language inputs and produces contextually relevant responses.
   
3. **Text-to-Speech Conversion:** The generated responses are converted into audio using the Google Text-to-Speech (gTTS) library, allowing the chatbot to speak the responses back to the user.


**Usage:**
1. Run the provided Python script in a suitable development environment or terminal.
   
2. Speak into the microphone connected to the system to communicate with the chatbot.
   
3. The chatbot will transcribe the spoken words, generate a response based on the input, and speak back the response to the user.
   
4. Enjoy conversing with the AI chatbot and explore its capabilities.

**Dependencies:**
- OpenAI API
- gTTS (Google Text-to-Speech)
- PyAudio
- Wave
- Gradio

**Setup:**
1. Obtain API keys for OpenAI's Audio API and gTTS (if applicable) and replace the placeholders in the code with the actual keys.
   
2. Install the required Python dependencies using pip (`pip install openai gradio gtts pyaudio`).
   
3. Ensure that the microphone and audio output devices are correctly configured and accessible by the system.


**Authors:**
- Kumaravendhan Ravichandran

**Acknowledgments:**
- Special thanks to OpenAI for providing access to their powerful language models and audio processing APIs.
- Gratitude to the developers of the gTTS, PyAudio, and Wave libraries for their contributions to the project's functionality.
