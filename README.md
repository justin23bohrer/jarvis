# Jarvis Voice Assistant

A local, voice-activated AI assistant for Windows that combines speech recognition, OpenAI GPT, and system automation. Talk to Jarvis to open websites, launch applications, control media playback, and have conversations.

## ✨ Features

- **🎤 Voice Activation**: Say "Jarvis [command]" for instant response
- **🤖 AI Conversations**: Powered by OpenAI GPT-4 for intelligent responses
- **🌐 Website Control**: "Jarvis go to google dot com" opens websites
- **💻 App Launcher**: "Jarvis open Spotify" launches any installed application
- **🎵 Media Control**: Play, pause, skip, and stop music with voice commands
- **🔊 Text-to-Speech**: Jarvis responds with natural speech synthesis
- **⚡ One-Shot Commands**: No need to wait between wake word and command

## 🚀 Quick Start

### Prerequisites
- Windows OS
- Python 3.8+
- Microphone
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/justin23bohrer/jarvis.git
   cd jarvis
   ```

2. **Install Python dependencies**
   ```bash
   pip install sounddevice vosk openai python-dotenv pyttsx3 keyboard
   ```

3. **Download Vosk speech model**
   - Visit [Vosk Models](https://alphacephei.com/vosk/models)
   - Download `vosk-model-en-us-0.22-lgraph` (or similar English model)
   - Extract to your project root directory

4. **Set up OpenAI API**
   - Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run Jarvis**
   ```bash
   python main.py
   ```

## 🗣️ Voice Commands

### Basic Usage
- **Start**: Say "Jarvis [your command]"
- **Exit**: Say "Jarvis stop"

### Website Navigation
```
"Jarvis go to youtube dot com"
"Jarvis go to github dot com" 
"Jarvis go to stackoverflow dot com"
```

### Application Control
```
"Jarvis open notepad"
"Jarvis open spotify"
"Jarvis open chrome"
```

### Media Control
```
"Jarvis play music"
"Jarvis pause music"
"Jarvis skip song"
"Jarvis previous song"
"Jarvis stop music"
```

### Conversations
```
"Jarvis what's the weather like?"
"Jarvis tell me a joke"
"Jarvis how do I cook pasta?"
```

## 📁 Project Structure

```
jarvis/
├── main.py                 # Entry point
├── voiceLoop.py           # Main command loop and routing
├── transcribe.py          # Speech recognition with Vosk
├── responder.py           # Text-to-speech synthesis
├── GPTcom.py             # OpenAI GPT integration
├── features/
│   ├── openWebsite.py    # Website opening functionality
│   ├── openApp.py        # Application launcher
│   └── mediaControl.py   # Media playback controls
├── .env                  # Environment variables (not tracked)
├── .gitignore           # Git ignore rules
└── vosk-model-*/        # Speech recognition model (not tracked)
```

## ⚙️ Configuration

### Adding Custom Applications
Edit `features/openApp.py` to add paths for your favorite applications:

```python
app_paths = {
    "spotify": r"C:\Users\YourName\AppData\Roaming\Spotify\Spotify.exe",
    "discord": r"C:\Users\YourName\AppData\Local\Discord\Update.exe",
    "vscode": r"C:\Program Files\Microsoft VS Code\Code.exe",
    # Add more apps here
}
```

### Customizing Voice Response
Modify the system message in `GPTcom.py` to change Jarvis's personality:

```python
{"role": "system", "content": "You are Jarvis, a helpful and witty AI assistant."}
```

### Adjusting Speech Recognition
Update the model path in `transcribe.py` to use different Vosk models for better accuracy or different languages.

## 🔧 Troubleshooting

### Common Issues

**"Model not found" error**
- Ensure the Vosk model folder is in your project root
- Check that the folder name matches the `model_path` in `transcribe.py`

**"Quota exceeded" error**
- Verify your OpenAI API key is valid and has remaining credits
- Check your OpenAI account dashboard

**App won't open**
- Add the full path to your app in `features/openApp.py`
- Verify the executable path is correct

**No audio input**
- Check microphone permissions
- Ensure your microphone is set as the default recording device

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Vosk](https://alphacephei.com/vosk/) for offline speech recognition
- [OpenAI](https://openai.com/) for GPT language models
- [pyttsx3](https://pypi.org/project/pyttsx3/) for text-to-speech
- Inspired by Tony Stark's J.A.R.V.I.S.

---

**Made with ❤️ by [Justin Bohrer](https://github.com/justin23bohrer)**
