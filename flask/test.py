from flask import Flask, render_template, request
  
app = Flask(__name__)
  
  # routeを作る; HTMLファイルを表示する
@app.route('auth')
def auth():
      return render_template('auth.html')
  
  # routeを作る; 結果を表示する
@app.route('/output', methods=['POST'])
def output():
      id = request.form['id']
      pwd = request.form['pwd']
      
      # IDとPWDを確認する （ほんとうに、お客さまですか？？）
      true_id = 'tanaka'			# 正しい ID
      true_pwd = 'masahiko'			# 正しい PWD
      
      if true_id==id and true_pwd==pwd:
          kekka = 'いらっしゃいませ！'			# 正しいとき
      else:
          kekka = 'IDかパスワードが、ちがいます'		# 問題あるとき
      
      return kekka
  
  
  # 実行する
if __name__=='__main__':
    app.run(debug=True)
  
