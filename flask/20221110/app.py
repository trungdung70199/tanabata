from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/touroku')
def touroku():
	return render_template('touroku.html')

@app.route('/touroku_app', methods=['POST'])
def touroku_app():
	id = request.form['id']
	pwd = request.form['pwd']
	return id+':'+pwd

@app.route('/radio')
def radio():
	return render_template('radio.html')

@app.route('/radio_app', methods=['POST'])
def radio_app():
	address = request.form['address']
	return address

@app.route('/select')
def slect():
	return render_template('select.html')

@app.route('/select_app', methods=['POST'])
def select_app():
	favorite = request.form['favorite']
	return favorite

@app.route('/textarea')
def textarea():
	return render_template('textarea.html')

@app.route('/textarea_app', methods=['POST'])
def textarea_app():
	data = request.form['data']
	return data

if __name__=='__main__':
	app.run(debug=True)
	


