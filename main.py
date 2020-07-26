from flask import Flask
from write import write
from flask import send_file
from io import BytesIO
from flask import make_response
import json
from db import increment, exist
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


app = Flask(__name__)


limiter = Limiter(
    app, key_func=get_remote_address, default_limits=["200 per day", "45 per hour"],
)


@app.route("/count/<name>")
@limiter.limit("1 per minute")
def tracker(name):

    if exist(name):
        app = increment(name)

        image = write(app["count_visited"])

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
    else:
        return "Not found"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
