from models import Planets

class PlanetService:
    def get_list(self):
        planet_list = Planets.query.all()
        return {
            "results": [planet.serialize() for planet in planet_list]
            }
  
    def get_by_id(self, planet_id):
        user = Planets.query.filter_by(id=planet_id).first()
        return {
            "message": "ok",
            "result": {
                "properties": {
                "diameter": "10200",
                "rotation_period": "24",
                "orbital_period": "4818",
                "gravity": "1 standard",
                "population": "1000",
                "climate": "temperate, tropical",
                "terrain": "jungle, rainforests",
                "surface_water": "8",
                "created": "2025-01-30T12:15:53.709Z",
                "edited": "2025-01-30T12:15:53.709Z",
                "name": "Yavin IV",
                "url": "https://www.swapi.tech/api/planets/3"
                },
                "description": "A planet.",
                "_id": "5f7254c11b7dfa00041c6fb0",
                "uid": "3",
                "__v": 0
            }
            }