import flask
from warehouse import Warehouse

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


@app.route("/submission", methods=["GET", "POST"])
def form_submit():
    whs = Warehouse()
    author = flask.request.form.get("author")
    title = flask.request.form.get("title")

    whs.add_book(title=title, author=author)

    return """
    <h1>Form submitted</h1>
    <a href="http://127.0.0.1:5000/#home">Go back</a>
    """


if __name__ == "__main__":
    app.run(debug=True)
