from datetime import datetime

def healthcheck_response(mig_ver):
    time_now = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    return {
        "ok":True,
        "result": {
            "migration_version": mig_ver,
            "time_now":time_now
        }
    }