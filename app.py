import os
import logging
from flask import Flask,render_template
from flask_migrate import Migrate
from config import Config
from models.models import db,AdminUser
from routes.category import category_bp
from routes.products import product_bp
from routes.admin import admin_bp
from routes.add_new import add_new_bp
from routes.modify import modify_data_bp
from routes.contact import contact_bp, limiter

from flask_login import LoginManager

# Configure the logging
logging.basicConfig(    
    filename='log.txt',
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s: %(message)s'
)

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.secret_key = "sahil"
    app.config.from_object(Config)
    
    # Set Upload Folder
    app.config["UPLOAD_FOLDER"] = os.path.join(os.getcwd(), "static/uploads")
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    db.init_app(app)
    # Migrate(app, db)
    #DEV: code for login 
    login_manager = LoginManager()
    login_manager.login_view = 'admin.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(AdminUser, int(user_id))


    # Register Blueprints
    app.register_blueprint(category_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(add_new_bp)
    app.register_blueprint(modify_data_bp)
    app.register_blueprint(contact_bp)



    @app.route('/designs/A-Frame')
    def aframe():
        return render_template('designs/A-frame.html') 

    @app.route('/designs/Prefabricated-Luxury-house')
    def Prefabricated():
        return render_template('designs/prefabricated-Luxury.html') 

    @app.route('/designs/Wooden-House')
    def wooden_house():
        return render_template('designs/wooden-house.html') 

    @app.route('/designs/Wooden-Resort')
    def wooden_resort():
        return render_template('designs/wooden-resort.html') 

    @app.route('/designs/A-Frame-Cottages')
    def aframecottages():
        return render_template('designs/a-frame-cottages.html') 

    @app.route('/designs/Portable-House')
    def portable_house():
        return render_template('designs/portable-house.html') 

    @app.route('/designs/Prefabricated-Wooden-house')
    def Prefab_wooden():
        return render_template('designs/prefab-wooden-house.html') 

    @app.route('/designs/Modular-Cottage')
    def modular():
        return render_template('designs/modular-cottage.html') 

    @app.route('/designs/Prefabricated-house')
    def Prefab_house():
        return render_template('designs/prefab-house.html') 

    @app.route('/designs/Portable-Cabin')
    def portable_cabin():
        return render_template('designs/portable-cabin.html') 

    @app.route('/designs/Office-Cabin')
    def office_cabin():
        return render_template('designs/office-cabin.html') 

    @app.route('/designs/Double-Storey-Houses')
    def double_storey():
        return render_template('designs/double-storey.html') 

    @app.route("/")
    def index():
        return render_template("index.html")
    return app


    

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
    logging.info("Flask App started")

