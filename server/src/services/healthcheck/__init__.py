from ...repos.healthcheck import HealthcheckRepo

class HealthcheckService:
    def __init__(self, db):
        self.repo = HealthcheckRepo(db)

    def healthCheck(self):
        return self.repo.migration_version()