from flask import Flask, render_template
from flask_transcrypt import FlaskTranscrypt

app = Flask(
    __name__,
    template_folder="assets/templates",
    static_folder="assets/static"
)

transcrypt = FlaskTranscrypt(app)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)