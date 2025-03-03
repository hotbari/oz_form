from config import db
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_smorest import Api
from app.routes import routes
import app.models

migrate = Migrate()


def create_app():
    application = Flask(__name__)

    application.config["API_TITLE"] = "OZ Form API"  # 원하는 제목으로 설정
    application.config["API_VERSION"] = "v1"  # API 버전 설정
    application.config["OPENAPI_VERSION"] = "3.0.2"  # OpenAPI 버전 설정

    application.config.from_object("config.Config")
    application.secret_key = "oz_form_secret"

    db.init_app(application)

    migrate.init_app(application, db)

    api = Api(application)

    @application.errorhandler(400)
    def handle_bad_request(error):
        response = jsonify({"message": error.description})
        response.status_code = 400
        return response

    # 블루 프린트 등록
    application.register_blueprint(routes)

    return application
