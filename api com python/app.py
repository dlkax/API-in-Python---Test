#importação
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#criando uma variavel (app) que irá receber a instancia
#da classe (Flask)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)

# modelagem 
# produto (id, name, price, description)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)


#definir uma rota raiz (pagina inicial) e a função 
#que será executada ao requisitar 
@app.route('/teste')
def nova_funcao():
    return 'Teste de API'

if __name__ == "__main__":
    app.run(debug=True)