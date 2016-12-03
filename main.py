from flask import Flask, current_app
app = Flask(__name__)

@app.route('/')
def hey():
	return current_app.send_static_file('index.html')