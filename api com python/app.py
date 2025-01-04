#importação
from flask import Flask


#criando uma variavel (app) que irá receber a instancia
#da classe (Flask)
app = Flask(__name__)

#definir uma rota raiz (pagina inicial) e a função 
#que será executada ao requisitar 
@app.route('/teste')
def nova_funcao():
    return 'Teste de API'

if __name__ == "__main__":
    app.run(debug=True)