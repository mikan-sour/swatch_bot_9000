class SilhouetteService:
    def __init__(self, silhouette_repo):
        self.silhouette_repo = silhouette_repo

    def get_all(self):
        return self.silhouette_repo.get_all()

    def get_one(self, silhouette_id):
        return self.silhouette_repo.get_one(silhouette_id)

    def update_one(self, silhouette_id, data):
        return self.silhouette_repo.update_one(silhouette_id, data)

    def create_one(self, data):
        return self.silhouette_repo.create_one(data)

    def create_many(self, data_list):
        return self.silhouette_repo.create_many(data_list)

    def delete(self, silhouette_ids):
        return self.silhouette_repo.delete(silhouette_ids)
