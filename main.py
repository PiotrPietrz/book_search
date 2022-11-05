import flask
from warehouse import Warehouse

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/result", methods=["GET", "POST"])
def result():
    items = [
        {"Title": "title1", "Author": "author1"},
        {"Title": "title2", "Author": "author2"},
    ]

    return flask.render_template("result.html", items=items)


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    return flask.render_template("add_book.html")


@app.route("/submission", methods=["GET", "POST"])
def form_submit():
    whs = Warehouse()
    author = flask.request.form.get("author")
    title = flask.request.form.get("title")

    whs.add_book(title=title, author=author)

    return flask.render_template("submission.html")


if __name__ == "__main__":
    app.run(debug=True)
