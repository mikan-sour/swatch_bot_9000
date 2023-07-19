
class HealthcheckRepo:
    def __init__(self, db):
        self.db = db

    def migration_version(self):
        query = "SELECT version FROM public.schema_migrations LIMIT 1;"
        result = self.db.execute(query)
        return result.fetchone()[0]
