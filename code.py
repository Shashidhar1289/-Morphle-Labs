from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess
import platform

app = Flask(__name__)

@app.route('/')
def system_info():
    name = "P.SHASHIDHAR REDDY"
    username = os.environ.get("USERNAME", os.environ.get("USER", "Admin"))  
    ist_time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S %Z')
    
    if platform.system() == "Windows":
        top_output = subprocess.getoutput('wmic process get Description, ProcessId')
    else:
        top_output = subprocess.getoutput('ps aux --sort=-%mem | head -10')
    
    formatted_output = f"""
    <html>
    <head>
        <title>System Information</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1 {{ color: #333; }}
            pre {{ background: #f4f4f4; padding: 10px; border-radius: 5px; }}
        </style>
    </head>
    <body>
        <h1>System Information</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {ist_time}</p>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return formatted_output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
