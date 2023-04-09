from flask import Flask
from pymongo import MongoClient
from utils import CustomEncoder

client = MongoClient()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.json_provider_class = CustomEncoder
    from blueprints.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    with app.app_context():
        db = client[app.config['MONGO_DBNAME']]
        from models import User
        User.initialize_db(db)

    return app

app = create_app()  

if __name__ == '__main__':
    app.run(port=5000)
