import time
from flask import Flask

import os
from flask import Flask, request, render_template

from flask import jsonify
from model import db

app = Flask(__name__)

@app.route('/')
def hello():
    return {"hello": "world"}

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
    
    print("CREATE TABLE MATRETT")
    
    db.create_all()

    return jsonify({
        'success': True,
        'file': 'Received'
    })

    if __name__ == '__main__':
        app.run(debug=True)