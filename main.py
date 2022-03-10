from ast import Pass
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)
api = Api(app)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cityhop_data.db'
# PASSWORD = "cityhop123"
# PUBLIC_IP_ADDRESS = "35.197.212.159"
# DBNAME ="cityhop_data"
# PROJECT_ID = "cityhop-341920"
# INSTANCE_NAME ="cityhop-341920:europe-west2:cityhop-db"

# app.config["SQLALCHEMY_DATABASE_URI"]= f"mysql + mysqldb://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket =/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

from database import db
from database import *

db.create_all()

login_put_args = reqparse.RequestParser()
login_put_args.add_argument("email", type=str, help="Error: email required", required=True)
login_put_args.add_argument("password", type=str, help="Error: password required", required=True)

register_put_args = reqparse.RequestParser()
register_put_args.add_argument("email", type=str, help="Error: email required", required=True)
register_put_args.add_argument("f_name", type=str, help="Error: forename required", required=True)
register_put_args.add_argument("l_name", type=str, help="Error: surname required", required=True)
register_put_args.add_argument("phone_num", type=str, help="Error: phone number required", required=True)
register_put_args.add_argument("password", type=str, help="Error: password required", required=True)


class Login(Resource):
    def put(self):
        args = login_put_args.parse_args()
        input_email = request.form['email']
        input_password = request.form['password']
        current_user = Users.query.filter_by(email=input_email).first()
        if current_user is not None:
            p = Passwords.query.filter_by(user_id=current_user.user_id).first()
            if input_password == p.password:
                return {"email": current_user.email, "f_name": current_user.first_name, "l_name": current_user.last_name, "phone_num": current_user.phone_number}
            else:
                return {"status": "Incorrect email/password"}
        else: 
            return {"status": "Incorrect email/password"}


class Register(Resource):
    def put(self):
        args = register_put_args.parse_args()
        email = request.form['email']
        f_name = request.form['f_name']
        l_name = request.form['l_name']
        phone_num = request.form['phone_num']
        password = request.form['password']
        existing_user = Users.query.filter_by(email=email).first()
        if existing_user is None:
            new_user = Users(first_name=f_name, last_name=l_name, email=email, phone_number=phone_num)
            db.session.add(new_user)
            db.session.commit()
            return {"status": "Success"}
        else: 
            return {"status": "Existing"}

class GetScooters(Resource):
     def get(self):
         scooters = Scooters.query.all()
         output = [{'scooter_id':s.scooter_id,'availability':s.availability, 'location_id':s.location_id} for s in scooters]
         return jsonify(output)

api.add_resource(Login, "/login")
api.add_resource(Register, "/register")
api.add_resource(GetScooters, "/scooters")

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
