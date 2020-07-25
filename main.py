from flask import Flask
from write import write
from flask import send_file
from io import BytesIO
from flask import make_response
import json
from db import write_db, get_apps

app = Flask(__name__)


apps_count = {}

apps_count = get_apps()


@app.route("/<name>")
def tracker(name):

    if name in apps_count:
        apps_count[name] += 1

        write_db(name, apps_count[name])

        image = write(apps_count[name])

        try:
            response = make_response(
                send_file(
                    BytesIO(image), attachment_filename="logo.jpg", mimetype="image/jpg"
                )
            )

            # Disable caching
            response.headers["Pragma-Directive"] = "no-cache"
            response.headers["Cache-Directive"] = "no-cache"
            response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
            response.headers["Pragma"] = "no-cache"
            response.headers["Expires"] = "0"
            return response
        except:
            pass


if __name__ == "__main__":
    app.run(host="0.0.0.0")
