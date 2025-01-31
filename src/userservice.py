from models import User

class UserService:
    def get_list(self):
        user_list = User.query.all()
        return [user.serialize() for user in user_list]