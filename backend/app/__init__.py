from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from app.resources import GetDataResource, GetCompaniesList, GetReportsList, FinDataResource
from flask_sqlalchemy import SQLAlchemy
from app.database import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    api = Api(app)
    CORS(app)

    api.add_resource(GetDataResource, '/get_data/<string:month>')
    api.add_resource(GetCompaniesList, '/api/companies')
    api.add_resource(GetReportsList, '/reports/companies', '/reports/companies/<string:company_name>')
    api.add_resource(FinDataResource, '/api/fin/<string:company_name>')
    return app

# if __name__ == '__main__':
#     app.run(debug=True)
