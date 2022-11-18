import flask
from warehouse import Warehouse
from scraper import Scraper

app = flask.Flask(__name__)

whs = Warehouse()
scr = Scraper()


@app.route("/")
def index():
    return flask.render_template("index.html")


@app.route("/result", methods=["GET", "POST"])
def result():
    title = flask.request.form.get("search_bar")

    items = whs.display(title=title)
    recs = scr.display(title=title)
    return flask.render_template("result.html", items=items, recs=recs)


@app.route("/add_book", methods=["GET", "POST"])
def add_book():
    return flask.render_template("add_book.html")


@app.route("/submission", methods=["GET", "POST"])
def form_submit():

    author = flask.request.form.get("author")
    title = flask.request.form.get("title")
    genre = flask.request.form.get("genre")

    whs.add_book(title=title, author=author, genre=genre)

    return flask.render_template("submission.html")


if __name__ == "__main__":
    app.run(debug=True)
