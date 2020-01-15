from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import json

app = Flask(__name__)

# with open('/etc/config.json') as config_file:
#     config = json.load(config_file)
#
# app.config['SECRET_KEY'] = config.get('SECRET_KEY')
# app.config['SQLALCHEMY_DATABASE_URI'] = config.get('SQLALCHEMY_DATABASE_URI')

app.config['SECRET_KEY'] = '1A37BbcCJh67'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

from flask_app import routes




if __name__ == '__main__':
    app.run(debug=True)

