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


def get_apps():
    apps = {}

    for app in db.apps.find():

        apps[app["name"]] = int(app["count_visited"])

    return apps


def write_db(app_name, count):
    app = db.apps.find_one_and_update(
        {"name": app_name}, {"$set": {"count_visited": count}}, upsert=False
    )


if __name__ == "__main__":
    apps = get_apps()

    value = int(apps["app1"])

    value += 1

    write_db("app1", value)

