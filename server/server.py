# from flask import Flask, jsonify
# from flask_cors import CORS
# import subprocess
# import sys

# app = Flask(__name__)
# CORS(app)

# python_executable = sys.executable  # Gets the correct Python path

# @app.route('/voice-assistant', methods=['GET'])
# def start_voice_assistant():
#     subprocess.Popen([python_executable, "voice_assistant.py"])
#     return jsonify({"message": "Voice Assistant Started"}), 200

# @app.route('/virtual-mouse', methods=['GET'])
# def start_virtual_mouse():
#     subprocess.Popen([python_executable, "mouse.py"])
#     return jsonify({"message": "Virtual Mouse Started"}), 200

# @app.route('/virtual-keyboard', methods=['GET'])
# def start_virtual_keyboard():
#     subprocess.Popen([python_executable, "keyboard.py"])
#     return jsonify({"message": "Virtual Keyboard Started"}), 200

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, jsonify, request
from flask_cors import CORS
import subprocess
import os
import signal
import sys

app = Flask(__name__)
CORS(app)

python_executable = sys.executable  # Gets the correct Python path

# Dictionary to store running processes
running_processes = {}

# Function to start a process
def start_process(name, script):
    if name in running_processes:
        return jsonify({"message": f"{name} is already running."}), 400
    
    process = subprocess.Popen([python_executable, script])
    running_processes[name] = process
    return jsonify({"message": f"{name} started."}), 200

# Function to stop a process
def stop_process(name):
    if name in running_processes:
        process = running_processes.pop(name)
        os.kill(process.pid, signal.SIGTERM)  # Terminate the process
        return jsonify({"message": f"{name} stopped."}), 200
    else:
        return jsonify({"message": f"{name} is not running."}), 400

# API routes
@app.route('/start/<option>', methods=['GET'])
def start_option(option):
    scripts = {
        "voice-assistant": "voice_assistant.py",
        "virtual-mouse": "mouse.py",
        "virtual-keyboard": "keyboard.py"
    }
    if option in scripts:
        return start_process(option, scripts[option])
    return jsonify({"message": "Invalid option"}), 400

@app.route('/stop/<option>', methods=['GET'])
def stop_option(option):
    return stop_process(option)

if __name__ == '__main__':
    app.run(debug=True)
