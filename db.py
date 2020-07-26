import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Load file from the path.
load_dotenv(".env")

# Accessing variables.
conection_uri = os.getenv("DB_CONNECT")
print(conection_uri)


# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(conection_uri)
db = client["api-tracker"]


def increment(app_name):
    app = db.apps.find_one_and_update(
        {"name": app_name}, {"$inc": {"count_visited": 1}}, upsert=False
    )

    app["count_visited"] += 1

    return app


def exist(app_name):
    print("searching for: " + app_name)
    if db.apps.find({"name": app_name}).count() > 0:
        return True

    else:
        return False


if __name__ == "__main__":
    # apps = get_apps()

    # value = int(apps["app1"])

    # value += 1

    # write_db("app1", value)
    increment("app1")

