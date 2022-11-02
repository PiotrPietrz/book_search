import flask

app = flask.Flask(__name__)


@app.route("/")
def home():
    return flask.render_template("index.html")


@app.route("/result", methods=["GET", "POST"])
def result():
    # t = flask.request.form.get("search_bar")
    # print(t)
    return flask.render_template("result.html")


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    return flask.render_template("add_book.html")


if __name__ == "__main__":
    app.run(debug=True)
