from flask import Flask, render_template, request

app = Flask(__name__)

# Conjunto de dados de filmes
filmes = [
    {"nome": "Mad Max", "genero": "Ação"},
    {"nome": "Toy Story", "genero": "Animação"},
    {"nome": "Invocação do Mal", "genero": "Terror"},
    {"nome": "O Rei Leão", "genero": "Animação"},
    {"nome": "Gente grande", "genero": "Comédia"},
    {"nome": "It", "genero": "Terror"},
    {"nome": "Gente grande 2", "genero": "Comèdia"},
    {"nome": "A forja", "genero": "Drama"},
    
]

@app.route('/', methods=['GET', 'POST'])
def index():
    sugestoes = []
    if request.method == 'POST':
        genero_preferido = request.form['genero'].capitalize()
        # Filtra os filmes com o gênero escolhido
        sugestoes = [f['nome'] for f in filmes if f['genero'] == genero_preferido]
    return render_template('index.html', sugestoes=sugestoes)

if __name__ == '__main__':
    app.run(debug=True)
