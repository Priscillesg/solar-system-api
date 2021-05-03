from app import db
from app.models.planet import Planet
from flask import request, Blueprint, make_response 
from flask import jsonify

planet_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planet_bp.route("/<planet_id>", methods=["GET"])
def handle_planets(planet_id):
    planet = Planet.query.get(planet_id)
    if planet:
        return ({
            "id": planet.id,
            "name": planet.name,
            "description": planet.description
        }, 200)
    return{
        "message": f"Planet {planet_id} not found",
        "success": False,
        }, 404
@planet_bp.route("",methods=["POST","GET"])
def planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description
            })
        return jsonify(planets_response), 200
    else:
        request_body = request.get_json()
        new_planet = Planet(name = request_body["name"],
                        description = request_body["description"]
                                                    )
        db.session.add(new_planet)
        db.session.commit()
        return (f'planet #{new_planet.name} has been created', 201 )

