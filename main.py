from flask import Flask
from write import write
from flask import send_file
from io import BytesIO
from flask import make_response
import json

app = Flask(__name__)


apps_count = {}

with open("apps.json") as file:
    apps_count = json.load(file)
print(apps_count)


@app.route("/<name>")
def tracker(name):

    if name in apps_count:
        apps_count[name] += 1

        # note that output.json must already exist at this point
        with open("apps.json", "w") as f:
            # this would place the entire output on one line
            # use json.dump(lista_items, f, indent=4) to "pretty-print" with four spaces per indent
            json.dump(apps_count, f)

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
