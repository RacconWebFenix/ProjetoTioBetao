from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    runas = [
        {
            'nome': 'Aard',
            'imagem': '/static/aard.png',
            'cardArt': '/static/cardart_aard.jpg'
        },
        {
            'nome': 'Axii',
            'imagem': '/static/axii.png',
            'cardArt': '/static/cardart_axii.jpg'
        },
        {
            'nome': 'Igni',
            'imagem': '/static/igni.png',
            'cardArt': '/static/cardart_igni.jpg'
        },
        {
            'nome': 'Quen',
            'imagem': '/static/quen.png',
            'cardArt': '/static/cardart_quen.jpg'
        },
        {
            'nome': 'Yrden',
            'imagem': '/static/yrden.png',
            'cardArt': '/static/cardart_yrden.jpg'
        },
    ]
    return render_template('index.html', runas=runas)


if __name__ == '__main__':
    app.run(debug=True)
