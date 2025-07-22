import subprocess
import os

def open_app(app_name: str):
    app_name = app_name.lower().strip()
    app_paths = {}
    path = app_paths.get(app_name)
    if not path or not os.path.exists(path):
        # Try to find the app using 'where' command
        try:
            result = subprocess.run(['where', app_name], capture_output=True, text=True)
            found_path = result.stdout.splitlines()[0] if result.stdout else None
            if found_path and os.path.exists(found_path):
                subprocess.Popen(found_path)
                return f"Opening {app_name}"
            else:
                return f"App '{app_name}' not found. Please add its path to the app list."
        except Exception as e:
            return f"Error finding app '{app_name}': {e}"
    else:
        subprocess.Popen(path)
        return f"Opening {app_name}"