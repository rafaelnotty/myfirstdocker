from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejecutar', methods=['POST'])
def ejecutar():
    output = subprocess.check_output(['python', 'codigo1.py'])
    return output

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')