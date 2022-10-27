from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def start():
    return 'Good morning.'

@app.route('/msg')
def msg():
    return render_template('msg.html')

@app.route('/output', methods=['POST'])
def output():
    msg = request.form['msg']
    if msg =='hello':
         kekka = 'こんにちは！'
    else:
     kekka = msg
    return kekka

if __name__=='__main__':
        app.run(debug=True)