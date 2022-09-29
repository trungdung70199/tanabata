from flask import Flask

app = Flask(__name__)

@app.route('/ALOHA')
def hello():
	return '<h1>ALOHA!<h1>'


if __name__=='__main__':
	app.run(debug=True)

