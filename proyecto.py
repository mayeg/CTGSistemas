# -*- coding: utf-8 -*-
import os

from flask import Flask
from flaskext.mysql import MySQL

from routes.coordinador_routes import coordinador
from routes.estudiante_routes import estudiante
from routes.jurado_routes import jurado
from routes.login_routes import login_r
from routes.secretaria_routes import secretaria
from routes.usuario_routes import usuario

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'views')
app = Flask(__name__, template_folder=tmpl_dir)
app.secret_key = 'proyecto_ufps'
mysql = MySQL()

# import routes
app.register_blueprint(login_r)
app.register_blueprint(usuario, url_prefix="/usuarios")
app.register_blueprint(jurado, url_prefix="/jurado")
app.register_blueprint(secretaria, url_prefix="/secretaria")
app.register_blueprint(coordinador, url_prefix="/coordinador")
app.register_blueprint(estudiante, url_prefix="/estudiante")

# MySQL configurations

app.config['MYSQL_DATABASE_USER'] = 'ufps_35'
app.config['MYSQL_DATABASE_PASSWORD'] = 'ufps_11'
app.config['MYSQL_DATABASE_DB'] = 'ufps_35'
app.config['MYSQL_DATABASE_HOST'] = 'sandbox2.ufps.edu.co'
mysql.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
