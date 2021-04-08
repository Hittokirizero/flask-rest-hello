"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, User_SW, Planets_SW, People_SW, Favorite_SW

#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200
""" API """
@app.route('/people', methods=['GET', 'POST'])
def people_sw():
    if request.method == 'GET':
        gt_get_people = People_SW.query.all()
        all_people = list(map(lambda x: x.serialize_people(), gt_get_people))
        return jsonify(all_people), 200
    elif request.method == 'POST':
        request_body = request.get_json()
        insert_people = People_SW(id_people=request_body["id_people"],
                                  people_height=request_body["people_height"],
                                  people_mass=request_body["people_mass"],
                                  people_hair_color=request_body["people_hair_color"],
                                  people_skin_color=request_body["people_skin_color"],
                                  people_eye_color=request_body["people_eye_color"],
                                  people_birth_year=request_body["people_birth_year"],
                                  people_gender=request_body["people_gender"],
                                  people_created=request_body["people_created"],
                                  people_edited=request_body["people_edited"],
                                  people_name=request_body["people_name"],
                                  people_homeworld=request_body["people_homeworld"],
                                  people_url=request_body["people_url"])
        db.session.add(insert_people)
        db.session.commit()
        return jsonify({"Todo ok" : request_body }), 200

@app.route('/people/<int:id_us>', methods=['GET'])
def people_sw_u(id_us):
    gt_get_people_u =  People_SW.query.filter_by(id_people = id_us).first()
    if gt_get_people_u is None:
        raise APIException('Lo que buscas no existe', status_code=404)
    people = gt_get_people_u.serialize_people()
    return jsonify(people), 200

@app.route('/planets', methods=['GET', 'POST'])
def get_planets_sw():
    if request.method == 'GET':
        gt_planets = Planets_SW.query.all()
        all_planets = list(map(lambda x: x.serialize_planets(), gt_planets))
        return jsonify(all_planets), 200
    elif request.method == 'POST':
        request_body = request.get_json()
        insert_planet_sw = Planets_SW(id_planets=request_body["id_planets"],
                                  planets_name=request_body["planets_name"],
                                  planets_diameter=request_body["planets_diameter"],
                                  planets_rotation_period=request_body["planets_rotation_period"],
                                  planets_orbital_period=request_body["planets_orbital_period"],
                                  planets_gravity=request_body["planets_gravity"],
                                  planets_population=request_body["planets_population"],
                                  planets_climate=request_body["planets_climate"],
                                  planets_terrain=request_body["planets_terrain"],
                                  planets_surface_water=request_body["planets_surface_water"],
                                  planets_created=request_body["planets_created"],
                                  planets_edited=request_body["planets_edited"],
                                  planets_url=request_body["planets_url"])
        db.session.add(insert_planet_sw)
        db.session.commit()
        return jsonify({"Todo ok" : request_body }), 200

@app.route('/planets/<int:id_pp>', methods=['GET'])
def get_planets_sw_u(id_pp):
    gt_get_planets_u =  Planets_SW.query.filter_by(id_planets = id_pp).first()
    if gt_get_planets_u is None:
        raise APIException('Lo que buscas no existe', status_code=404)
    planets = gt_get_planets_u.serialize_planets()
    return jsonify(planets), 200

@app.route('/user_sw', methods=['GET'])
def user_sw():
    gt_get_user = User_SW.query.all()
    all_user = list(map(lambda x: x.serialize_user(), gt_get_user))
    return jsonify(all_user), 200

@app.route('/user_sw/<int:user_id>/favorites', methods=['GET', 'POST', 'DELETE'])
def user_sw_fv(user_id):
    gt_get_user_sw_fv =  Favorite_SW.query.filter_by(user_id_fk = user_id)
    if gt_get_user_sw_fv is None:
        raise APIException('Lo que buscas no existe', status_code=404)

    if request.method == 'GET':
        gt_get_user_sw_fv =  Favorite_SW.query.filter_by(user_id_fk = user_id)
        if gt_get_user_sw_fv is None:
            raise APIException('Lo que buscas no existe', status_code=404)
        user_fav = list(map(lambda x: x.serialize_favorite(), gt_get_user_sw_fv))
        return jsonify(user_fav), 200
    elif request.method == 'POST':
        gt_get_user_sw_fv =  User_SW.query.filter_by(id_user = user_id).first()
        if gt_get_user_sw_fv is None:
            raise APIException('Lo que buscas no existe', status_code=404)

        request_body = request.get_json()
        insert_favorites = Favorite_SW(id_favorite=request_body["id_favorite"],
                                  user_id_fk=request_body["user_id_fk"],
                                  planets_id_fk=request_body["planets_id_fk"],
                                  people_id_fk=request_body["people_id_fk"],
                                  type_favorite=request_body["type_favorite"])
        db.session.add(insert_favorites)
        db.session.commit()
        return jsonify({"Todo ok" : request_body }), 200

@app.route('/favorites/<int:fav_id>', methods=['DELETE'])
def user_sw_fv_del(fav_id):
    gt_get_user_sw_fv_del =  Favorite_SW.query.filter_by(id_favorite = fav_id).first()
    if gt_get_user_sw_fv_del is None:
        raise APIException('Lo que buscas no existe', status_code=404)
    db.session.delete(gt_get_user_sw_fv_del)
    db.session.commit()
    return jsonify({"Elementos elimando numero de ID:": fav_id}), 200


"""
"id_favorite": self.id_favorite ,
            "user_id_fk": self.user_id_fk ,
            "planets_id_fk": self.planets_id_fk ,
            "people_id_fk": self.people_id_fk ,
            "type_favorite": self.type_favorite

@app.route('/get_favorites', methods=['GET'])
def get_favorites_sw():
    gt_favorites = Favorite_SW.query.all()
    all_favorites = list(map(lambda x: x.serialize_favorite(), gt_favorites))
    return jsonify(all_favorites), 200

@app.route('/post_task', methods=['POST'])
def post_task_td():
    request_body = request.get_json()
    insert_task = Todolist(td_task=request_body["label"], is_done=request_body["done"])
    db.session.add(insert_task)
    db.session.commit()
    return jsonify({"Todo ok" : request_body }), 200


@app.route('/del_task/<int:numb>', methods=['DELETE'])
def del_task_td(numb):
    task = Todolist.query.filter_by(id = numb).first()
    if task is None:
        raise APIException('Lo que buscas no existe', status_code=404)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"Elementos elimando numero de ID:": numb}), 200

"""




# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
