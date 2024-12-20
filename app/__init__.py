# app/__init__.py

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Validate configuration
    Config.validate()

    print("DEBUG (create_app): SQLALCHEMY_DATABASE_URI in config:", app.config.get("SQLALCHEMY_DATABASE_URI"))

    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)

    # Initialize Flask-RESTx API
    api = Api(
        app,
        version='1.0',
        title='Dam Management API',
        description='API documentation for Dam Management System',
        doc='/api/docs'  # Swagger UI will be available at /api/docs
    )

    # Import and register namespaces
    from .routes.main import main_bp
    from .routes.dams import dams_bp
    from .routes.latest_data import latest_data_bp
    from .routes.dam_resources import dam_resources_bp
    from .routes.specific_dam_analysis import specific_dam_analysis_bp
    from .routes.overall_dam_analysis import overall_dam_analysis_bp
    from .routes.dam_groups import dam_groups_bp
    from .routes.dam_group_members import dam_group_members_bp

    # Register namespaces with specific paths
    api.add_namespace(main_bp, path='/api')  # Root route
    api.add_namespace(dams_bp, path='/api/dams')
    api.add_namespace(latest_data_bp, path='/api/latest_data')
    api.add_namespace(dam_resources_bp, path='/api/dam_resources')
    api.add_namespace(specific_dam_analysis_bp, path='/api/specific_dam_analysis')
    api.add_namespace(overall_dam_analysis_bp, path='/api/overall_dam_analysis')
    api.add_namespace(dam_groups_bp, path='/api/dam_groups')
    api.add_namespace(dam_group_members_bp, path='/api/dam_group_members')

    return app
