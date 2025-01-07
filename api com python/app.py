#importação
from flask import Flask, request
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



@app.route('/api/products/add', methods=["POST"])
def add_product():
    data = request.json

    product = Product(
        name=data.get("name"),
        price=data.get("price"),
        description=data.get("description")
    )

    #adicionar ao banco de dados
    db.session.add(product)
    db.session.commit()

    return "Produto cadastrado com sucesso"

#definir uma rota raiz (pagina inicial) e a função
#que será executada ao requisitar
@app.route('/')
def nova_funcao():
    return 'Teste de API'

if __name__ == "__main__":
    # cria as tabelas no banco de dados se ainda nao existirem
    with app.app_context():
        db.create_all()

    app.run(debug=True)