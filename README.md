# Voice Assistant

## Overview
This is a simple voice assistant application built using Streamlit, OpenAI's GPT-3.5 language model, and audio processing libraries. The application allows users to interact with the voice assistant by recording their voice, which is then transcribed and used as input for generating AI responses. The AI responses are generated using OpenAI's GPT-3.5 model, and the final response is converted into speech using OpenAI's text-to-speech (TTS) capabilities.

## Features
- Voice recording: Users can record their voice through the application interface.
- Voice transcription: The recorded voice is transcribed into text using OpenAI's audio transcription capabilities.
- AI chat response: The transcribed text is used as input to generate AI responses using OpenAI's GPT-3.5 model.
- Text-to-speech: The AI-generated response is converted into speech using OpenAI's text-to-speech (TTS) capabilities.
- Playback: Users can listen to the AI-generated response through the application interface.

## Installation
1. Clone the repository:
    ```
    git clone https://github.com/your/repository.git
    ```

2. Install the required Python packages:
    ```
    pip install openai
    pip install audio-recorder-streamlit
    pip install streamlit
    ```

3. Set up OpenAI API key:
    - Sign up for an account on the OpenAI platform if you haven't already.
    - Get your API key from the OpenAI dashboard.
    - Set your API key as an environment variable named `API_KEY`.

## Usage
1. Run the application:
    ```
    streamlit main.py
    ```

2. Click on the voice recorder to start recording your query.
3. Once recording is complete, the application will transcribe your voice into text and display it.
4. The transcribed text is then sent to OpenAI's GPT-3.5 model for generating a response.
5. The AI-generated response is converted into speech and played back through the application interface.

## Credits
- Streamlit: [https://streamlit.io/](https://streamlit.io/)
- OpenAI: [https://openai.com/](https://openai.com/)
- Audio Recorder Streamlit: [https://pypi.org/project/audio-recorder-streamlit/](https://pypi.org/project/audio-recorder-streamlit/)

## Author
- **Chaitanya N**

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
