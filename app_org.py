from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/hello")

def hello():
    return "Hi world"

@app.route("/data/appInfo/<name>", methods=["GET"])
def queryDataMessageByName(name):
    print("type(name):", type(name))
    return f"string: {name}"

@app.route("/data/appInfo/id/<int:id>", methods=["GET"])
def queryDataMessageById(id):
    print("type(id):", type(id))
    return f"int: {id}"

@app.route("/data/appInfo/version/<float:version>", methods=["GET"])
def queryDataMessageByVersion(version):
    print("type(version): ", type(version))
    return f"float: {version}"

@app.route('/text')
def text():
    return '<html><body><h1>Hello World</h1></body></html>'

if __name__ == "__main__":
    app.run