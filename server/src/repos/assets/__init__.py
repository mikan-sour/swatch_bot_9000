
class AssetRepo:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        # Implement your logic to retrieve all asset records from the database
        # Use self.db to interact with the database
        query = "SELECT * FROM sb9.assets WHERE type = 'SILHOUETTE';"
        result = self.db.execute(query)
        return result.fetchall()

    def get_one(self, silhouette_id):
        # Implement your logic to retrieve a specific asset record from the database
        # Use self.db to interact with the database
        query = "SELECT * FROM sb9.assets WHERE id = %s;"
        result = self.db.execute(query, (silhouette_id,))
        return result.fetchone()

    def update_one(self, silhouette_id, data):
        # Implement your logic to update a specific asset record in the database
        # Use self.db to interact with the database
        query = "UPDATE sb9.assets SET name = %s, file_path = %s WHERE id = %s;"
        self.db.execute(query, (data['name'], data['description'], silhouette_id))
        return self.get_one(silhouette_id)

    def create_one(self, asset):
        query = "INSERT INTO sb9.assets (asset_name, file_path, upload_type) VALUES (%s, %s, %s) RETURNING *;"
        cursor = self.db.execute(query, (asset['asset_name'], asset['file_path'], asset['upload_type']))
        return cursor.fetchone()


