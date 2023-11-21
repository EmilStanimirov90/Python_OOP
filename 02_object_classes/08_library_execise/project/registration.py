from project.user import User
from project.library import Library
class Registration:
    @staticmethod # without usage of self
    def add_user(self, user: User, library: Library):
        for u in library.user_records:
            if u.user_id == user.user_id:
                return f"User with id = {u.user_id} already registered in the library!"
            library.user_records.append(user)

    def remove_user(self,user: User, library: Library):
        for u in library.user_records:
            if u.user_id == user.user_id:
                library