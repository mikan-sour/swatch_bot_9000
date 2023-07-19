
class Asset:
    def __init__(self, repo, storage_client, upload_type, asset_name, file, file_path):
        self.repo = repo
        self.storage_client = storage_client
        self.upload_type = upload_type.upper()
        self.asset_name = asset_name
        self.file = file
        self.file_path = file_path + '/' + self.file.filename
        self.created_by = None
        self.created_at = None
        self.updated_by = None
        self.updated_at = None

    def upload_to_s3(self):
        return self.storage_client.upload_fileobj(self.file,  self.file_path + '/' + self.file.filename)

    def store_in_database(self):
        result = self.repo.create_one(vars(self))
        self.created_by = result['created_by']
        self.created_at = result['created_at']
        return dict(result)

