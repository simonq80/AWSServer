from flask import Flask
from d import d
app = Flask(__name__)

app.register_blueprint(d, url_prefix='/d')

@app.route("/")
def xd():
	return "asdf"


if __name__ == "__main__":
	app.run()