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

    if flask.request.form.get("search_bar") is None:
        return """
                <h1>No results</h1>
                <a href="{{ url_for('index') }}">Go to the home page </a>
                <a href="{{ url_for('add_book') }}">Add another book</a>
                """
    else:
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

    return """
    <h1>Form submitted</h1>
    <a href="{{ url_for('index') }}">Go to the home page </a>
    <a href="{{ url_for('add_book') }}">Add another book</a>
    """


if __name__ == "__main__":
    app.run(debug=True)
