from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ordenacao')
def ordenacao():
    return render_template('ordenacao.html')

@app.route('/fila')
def fila():
    return render_template('fila.html')

if __name__ == '__main__':
    app.run(debug=True)