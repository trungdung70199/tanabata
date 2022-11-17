from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def input():
	return render_template('input.html')

@app.route('/input_app', methods=['POST'])
def input_app():
	input = request.form['input']
	return input

if __name__=='__main__':
	app.run(debug=True)
	


