from ...models.users import User

class UserRepository:
    def __init__(self, db):
        self.db = db

    def create_user(self, user):
        query = "INSERT INTO users (name, email, password) VALUES (?, ?, ?)"
        values = (user.name, user.email, user.password)
        cursor = self.db.execute(query, values)
        user_id = cursor.lastrowid
        return user_id

    def get_user(self, email):
        query = "SELECT * FROM users WHERE email = ?"
        values = (email,)
        cursor = self.conn.cursor()
        cursor.execute(query, values)
        row = cursor.fetchone()
        cursor.close()
        if row:
            return User(*row)
        return None