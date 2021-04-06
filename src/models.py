from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class User_SW(db.Model):
    __tablename__ = 'user_sw'
    id_user = db.Column(db.Integer, primary_key=True)
    name_user = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    email_user = db.Column(db.String(250), nullable=False)
    birth_user = db.Column(db.String(250), nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User_SW %r>' % self.name_user

    def serialize_user(self):
        return {
            "id_user": self.id_user,
            "name_user": self.name_user,
            "email": self.email_user,
            "birth_user": self.birth_user,
            "is_active": self.is_active
        }

class Planets_SW(db.Model):
    __tablename__ = 'planets_sw'
    id_planets = db.Column(db.Integer, primary_key=True)
    planets_name = db.Column(db.String(250), nullable=False)
    planets_diameter = db.Column(db.Integer, nullable=False)
    planets_rotation_period = db.Column(db.Integer, nullable=False)
    planets_orbital_period = db.Column(db.Integer, nullable=False)
    planets_gravity = db.Column(db.String(250), nullable=False)
    planets_population = db.Column(db.Integer, nullable=False)
    planets_climate = db.Column(db.String(250), nullable=False)
    planets_terrain = db.Column(db.String(250), nullable=False)
    planets_surface_water = db.Column(db.Integer, nullable=False)
    planets_created = db.Column(db.String(250), nullable=False)
    planets_edited = db.Column(db.String(250), nullable=False)
    planets_url = db.Column(db.String(250), nullable=False)


    def __repr__(self):
        return '<Planets_SW %r>' % self.planets_name

    def serialize_planets(self):
        return {
            "id_planets": self.id_planets,
            "planets_name": self.planets_name,
            "planets_diameter": self.planets_diameter,
            "planets_rotation_period": self.planets_rotation_period,
            "planets_orbital_period": self.planets_orbital_period,
            "planets_gravity": self.planets_gravity,
            "planets_population": self.planets_population, 
            "planets_climate": self.planets_climate,
            "planets_terrain": self.planets_terrain, 
            "planets_surface_water": self.planets_surface_water,
            "planets_created": self.planets_created,
            "planets_edited": self.planets_edited,
            "planets_url": self.planets_url
        }


class People_SW(db.Model):
    __tablename__ = 'people_sw'
    id_people = db.Column(db.Integer, primary_key=True)
    people_height = db.Column(db.Integer, nullable=False)
    people_mass = db.Column(db.Integer, nullable=False)
    people_hair_color = db.Column(db.String(250), nullable=False)
    people_skin_color = db.Column(db.String(250), nullable=False)
    people_eye_color = db.Column(db.String(250), nullable=False)
    people_birth_year = db.Column(db.String(250), nullable=False)
    people_gender = db.Column(db.String(250), nullable=False)
    people_created = db.Column(db.String(250), nullable=False)
    people_edited = db.Column(db.String(250), nullable=False)
    people_name = db.Column(db.String(250), nullable=False)
    people_homeworld = db.Column(db.String(250), nullable=False)
    people_url = db.Column(db.String(250), nullable=False)
    planets_id_fk = db.Column(db.Integer, db.ForeignKey('planets_sw.id_planets'), nullable=True)
    planets = db.relationship('Planets_SW')
 
    def __repr__(self):
        return '<People_SW %r>' % self.people_name

    def serialize_people(self):
        return {
            "id_people": self.id_people,
            "people_height": self.people_height,
            "people_mass": self.people_mass,
            "people_hair_color": self.people_hair_color,
            "people_skin_color": self.people_skin_color,
            "people_eye_color": self.people_eye_color,
            "people_birth_year": self.people_birth_year,
            "people_gender": self.people_gender,
            "people_created": self.people_created,
            "people_edited": self.people_edited,
            "people_name": self.people_name,
            "people_homeworld": self.people_homeworld,
            "people_url": self.people_url,
            "planets_id_fk": self.planets_id_fk
        }

# Ultima linea #
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Favorite_SW(db.Model):
    __tablename__ = 'favorite_sw'
    id_favorite = db.Column(db.Integer, primary_key=True)
    user_id_fk = db.Column(db.Integer, db.ForeignKey('user_sw.id_user'), nullable=False)
    planets_id_fk = db.Column(db.Integer, db.ForeignKey('planets_sw.id_planets'), nullable=False)
    people_id_fk = db.Column(db.Integer,db.ForeignKey('people_sw.id_people'), nullable=False)
    type_favorite = db.Column(db.String(250), nullable=False)
    user = db.relationship('User_SW')
    planets = db.relationship('Planets_SW')
    people = db.relationship('People_SW')

    def __repr__(self):
        return '<Favorite_SW %r>' % self.user_id_fk

    def serialize_favorite(self):
        return {
            "id_favorite": self.id_favorite ,
            "user_id_fk": self.user_id_fk ,
            "planets_id_fk": self.planets_id_fk ,
            "people_id_fk": self.people_id_fk ,
            "type_favorite": self.type_favorite ,
    }