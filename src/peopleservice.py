from models import People

class PeopleService:
    def get_list(self):
        people_list = People.query.all()
        return {
            "results": [person.serialize() for person in people_list]
            }
    

    def get_by_id(self, people_id):
        user = People.query.filter_by(id=people_id).first()
        return {
            "message": "ok",
            "result": {
                "properties": {
                "height": "172",
                "mass": "77",
                "hair_color": "blond",
                "skin_color": "fair",
                "eye_color": "blue",
                "birth_year": "19BBY",
                "gender": "male",
                "created": "2025-01-29T11:45:26.833Z",
                "edited": "2025-01-29T11:45:26.833Z",
                "name": "Luke Skywalker",
                "homeworld": "https://www.swapi.tech/api/planets/1",
                "url": "https://www.swapi.tech/api/people/1"
                },
                "description": "A person within the Star Wars universe",
                "_id": "5f63a36eee9fd7000499be42",
                "uid": "1",
                "__v": 0
            }
            }


        


                    