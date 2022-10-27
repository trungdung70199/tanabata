from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/auth2')
def auth2():
        return render_template('auth2.html')

@app.route('/output2', methods=['POST'])
def output2():

      id = request.form['id']
      pwd = request.form['pwd']

      file = open('id.txt', 'r')

      flag = 0

      for line in file:
            if id in line and pwd in line:
                        
                  flag = 1
                  break
            else:
                  flag = 0
      if flag==1:
            kekka = 'ID & Password, OK'
      else:
            kekka = 'ID or Password, 違います'
            
      file.close()
      return kekka

if __name__=='__main__':
        app.run(debug=True)
