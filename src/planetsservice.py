from models import Planets

class PlanetService:
    def get_list(self):
        planet_list = Planets.query.all()
        return {
            "results": [planet.serialize() for planet in planet_list]
            }
  
    def get_by_id(self, planet_id):
        planet_by_id = Planets.query.filter_by(id=planet_id).first()
        return planet_by_id.serialize()