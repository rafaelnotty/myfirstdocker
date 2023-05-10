from flask import Flask, render_template
import subprocess
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejecutar', methods=['POST'])
def ejecutar():
    output = subprocess.check_output(['python', 'codigo1.py'])
    return output

# Función para la página de la tabla
@app.route('/tabla')
def tabla():
    data = {'fecha': ['02/22/20', '5/23/20', '5/24/20'], 'valor1': [10, 20, 30], 'valor2': [15, 25, 35]}
    df = pd.DataFrame(data)
    table = df.to_html()
    return render_template('tabla.html', table=table)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')