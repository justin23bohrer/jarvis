from transcribe import listen_for_jarvis_command
from GPTcom import ask_gpt
from responder import speak
from features.openWebsite import open_website
from features.openApp import open_app
from features.mediaControl import handle_media_command

def run_jarvis():
    while True:
        command = listen_for_jarvis_command()
        if command.strip().lower() == "stop":
            print("Stopping Jarvis.")
            break
        # Open app command
        media_response = handle_media_command(command)
        if media_response:
            continue
        if command.lower().startswith("open "):
            app_name = command.split("open ", 1)[1].strip()
            result = open_app(app_name)
            speak(result)
            continue
        # Check for website command
        if command.lower().startswith("go to "):
            site = command.split(" ", 2)[2].strip()
            opened_site = open_website(site)
            speak(f"Opening {opened_site}")
            continue
        gpt_reply = ask_gpt(command)
        speak(gpt_reply)