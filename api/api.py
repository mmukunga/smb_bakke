import time
from flask import Flask

import os
from flask import Flask, request, render_template

from flask import jsonify

app = Flask(__name__)

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/api/upload', methods=['POST'])
def handle_form():
    print(request)
    files = request.files
    print(files)
    file = files.get('file')
    """
      CODE TO HANDLE FILE
    """
    print("Simon Mukunga")
    print(file)
    
    print("Simon Mukunga")
    

    return jsonify({
        'success': True,
        'file': 'Received'
    })