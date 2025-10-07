from flask import Flask, jsonify, request

app = Flask(__name__)



jogos = [

    {
        "id_jogo": 1,
        "nome": "The Legend of zelda: Breath of the Wild",
        "ano_lancamento": 2017,
        "genero": "Aventura / Mundo Aberto",
        "criador": "Nintendo",
        "imagem": "https://upload.wikimedia.org/wikipedia/pt/thumb/0/0f/Legend_of_Zelda_Breath_of_the_Wild_capa.png/270px-Legend_of_Zelda_Breath_of_the_Wild_capa.png"
    },

    {
        "id_jogo": 2,
        "nome": "God of War",
        "ano_lancamento": 2018,
        "genero": "Ação / Aventura",
        "criador": "Santa Mônica Studios",
        "imagem": "https://upload.wikimedia.org/wikipedia/pt/thumb/8/82/God_of_War_2018_capa.png/330px-God_of_War_2018_capa.png"

    },

    {
        "id_jogo": 3,
        "nome": "Grand Theft Auto III",
        "ano_lancamento": 2001,
        "genero": "Ação / Mundo Aberto",
        "criador": "Rockstar Games",
        "imagem": "https://upload.wikimedia.org/wikipedia/pt/thumb/c/cc/Grand_Theft_Auto_III_capa.png/330px-Grand_Theft_Auto_III_capa.png"
    }

]

# consultar todos

@app.route('/jogos', methods={'GET'})
def consultar_jogos():
    return jsonify(jogos)

app.run(port=5000,host='localhost',debug=True)