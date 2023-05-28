#!/usr/bin/env python3
# Main

from flask import Flask

# Create the Flask app
app = Flask(__name__)

# Define the main route
@app.route('/')
def index():
    return 'Welcome to EffiMax!'

# Start the Flask app
if __name__ == '__main__':
    app.run()
