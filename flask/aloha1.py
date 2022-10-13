from flask import Flask, render_template, request
app = Flask(__name__, static_folder='./templates/images')

@app.route('/')
def start():
	return 'ALOHA!'

@app.route('/hello')
def hello():
	msg = 'こんにちは！'
	return msg

@app.route('/weather')
def weather():
	msg = '雨が降ってます'
	return msg

@app.route('/mee')
def me():
	return render_template('mee.html')

@app.route('/favorite')
def favorite():
	return render_template('favorite.html')

@app.route('/form')
def form():
	return render_template('form.html')

@app.route('/result', methods=['POST'])
def result():
	id = request.form['id']
	return id

if __name__=='__main__':
	app.run(debug=True)


