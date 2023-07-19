class UserService:
    def __init__(self, repo):
        self.repo = repo

    def new_user(self, user):
        return self.repo.create_user(user.username, user.password)

    def login(self, user):
        user = self.repo.get_user(user.username, user.password)
        if not user:
            return False
        return user