class AssetService:
    def __init__(self, asset_repo):
        self.asset_repo = asset_repo

    def get_all(self):
        return self.asset_repo.get_all()

    def get_one(self, asset_id):
        return self.asset_repo.get_one(asset_id)

    def update_one(self, asset_id, data):
        return self.asset_repo.update_one(asset_id, data)

    def create_one(self, data):
        return self.asset_repo.create_one(data)

    def create_many(self, data_list):
        return self.asset_repo.create_many(data_list)

    def delete(self, asset_ids):
        return self.asset_repo.delete(asset_ids)
