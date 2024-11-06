from flask import Flask, render_template

#nome padrao
app = Flask(__name__)

#1 pagina do site
# route(link do site) -> hashtagtreinamentos.com/
# função -> o que você quer exibir naquela página
# template

#"@app.route()" é um decorator, é uma linha de codigo cuja a tem a finalidade de atribuir uma
#nova funcionalidade a funcao que vem logo embaixo dela, no caso: "def pagina_inicial()"
@app.route("/")
def pagina_inicial():
    return render_template('pagina_inicial.html')

@app.route("/contato")
def contatos():
    return render_template('contatos.html')

#deixe a rota com as setinhas em torno da "variavel", como "<nome_usuario>"
@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    #para passar o metodo "nome_usuario" da def para o html, defina uma variavel apó o render
    return render_template('usuarios.html', nome_usuario=nome_usuario)

#rodar o site
if __name__ == "__main__":
    app.run(debug=True)

#colocando em um servidor, exemplo "heroku"