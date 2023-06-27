from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ordenacao')
def ordenacao():
    return render_template('ordenacao.html')

@app.route('/matriz')
def matriz():
    return render_template('matriz.html')

@app.route('/arquivos')
def arquivos():
    return render_template('arquivos.html')

@app.route('/arvore')
def arvore():
    return render_template('arvore.html')

@app.route('/pesquisa')
def pesquisa():
    return render_template('pesquisa.html')

if __name__ == '__main__':
    app.run(debug=True)