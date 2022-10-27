id = input('IDを入力してください')
print(id)

pwd = input("パスワードを入力してください:")
print(pwd)

file = open("id.txt", "r")
flag = 0

for line in file:
  if id in line and pwd in line:
    #print("ID とパスワード: OK!")
    #print(line)
    flag = 1
    print("ID & password: OK")
    break
  else:
    flag = 0
    #print("違います")
if flag == 1:
#if id in line and pwd in line:
  print("ID & Password, OK")
else:
  print("ID or Password 違います")
data = file.read()
file.close()

if id in data and pwd in data:
  print("ID とパスワードが、データの中に、ありました！")


