# from flask import Flask, jsonify
# from flask_cors import CORS
# import subprocess

# app = Flask(__name__)
# CORS(app)

# @app.route('/voice_assistant', methods=['GET'])
# def voice_assistant():
#     try:
#         # Run the voice assistant script
#         subprocess.Popen(["python", "server/voice_assistant/shadow.py"])
#         return jsonify({"message": "Voice Assistant Started"}), 200
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask, jsonify
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)

@app.route('/voice_assistant', methods=['GET'])
def voice_assistant():
    try:
        # Get the absolute path of shadow.py
        script_path = os.path.abspath("/server/voice_assistant/shadow.py")

        # Ensure the file exists before running
        if not os.path.exists(script_path):
            return jsonify({"error": f"File not found: {script_path}"}), 404

        # Run the script with proper execution handling
        subprocess.Popen(["python", script_path], shell=True)

        return jsonify({"message": "Voice Assistant Started"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
