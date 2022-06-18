class UserService:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def getuser(self):
        users_info = self.user_repository.getuser()
        return users_info
