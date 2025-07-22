import keyboard

def handle_media_command(command: str):
    cmd = command.lower()
    if "play music" in cmd or "pause music" in cmd:
        keyboard.send("play/pause media")
        return "Toggling play/pause."
    elif "next song" in cmd or "skip song" in cmd:
        keyboard.send("next track")
        return "Skipping to next song."
    elif "previous song" in cmd:
        keyboard.send("previous track")
        return "Going to previous song."
    elif "stop music" in cmd:
        keyboard.send("stop media")
        return "Stopping music."
    else:
        return None