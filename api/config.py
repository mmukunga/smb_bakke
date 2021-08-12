from flask import Flask
 
 
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # sql config params
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://psewduzyqzsata:29c4ae64d5636e54f5125ea489256d1e9428cb9473ea98cbad7f2b68d01caeaf@ec2-34-251-245-108.eu-west-1.compute.amazonaws.com:5432/de6iafjirotfia'
    return app