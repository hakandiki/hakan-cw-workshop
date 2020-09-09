from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello World!'

@app.route("/second")
def second():
    return "This is second page."

@app.route("/third/subthird")
def subthird():
    return "the subthird of the page"

@app.route("/forth/<string:id>")
def forth(id):
    return f"id of this page {id}"

if __name__ == "__main__":
    app.run(debug=True)