from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    escolha = None
    cardRuna = None
    if request.method == 'POST':
        escolha = request.form['escolha']
        if escolha == 'Aard':
            cardRuna = 'static/cardart_aard.jpg'
        elif escolha == 'Axii':
            cardRuna = 'static/cardart_axii.jpg'
        elif escolha == 'Igni':
            cardRuna = 'static/cardart_igni.png'
        elif escolha == 'Quen':
            cardRuna = 'static/cardart_quen.jpg'
        elif escolha == 'Yarden':
            cardRuna = 'static/cardart_yrden.jpg'
    return render_template('index.html',
        escolha = escolha,
        cardRuna = cardRuna
    )

if __name__ == '__main__':
    app.run(debug=True)