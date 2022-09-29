from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello')
def hello():
	return '<h1>hello!</h1>'

@app.route('/ciao')
def ciao():
	return '<h1>Ciao!</h1>'

@app.route('/aso')
def aso():
	return '<h1>あ、 そう</h1>'

@app.route('/aloha')
def aloha():
	return render_template('aloha.html')

if __name__=='__main__':
	app.run(debug=True)
	


