from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)

# Session 密鑰
app.secret_key = "My secret KEY"

# Home Page
@app.route("/")
def index():
    return render_template('index.html')

# Sign in
# 判斷登入成功與否
@app.route("/signin", methods=['POST'])
def signin():
    username = request.form.get('username')
    password = request.form.get('password')
    # 當帳號密碼正確時 , SIGNED-IN 狀態為 True , 並轉至 member_page
    if username == 'test' and password == 'test':
        session['SIGNED-IN'] = True
        return redirect('/member')
    else:
        if username == '' or password == '':
          errorMessage = 'Please enter username and password.'
          return redirect('/error?message=' + errorMessage)
        else: 
          errorMessage = 'Username or password is not correct.'
          return redirect('/error?message=' + errorMessage)

# 登出
@app.route("/signout", methods=['GET'])
def signout():
    session['SIGNED-IN'] = False
    return redirect('/')

# 成功登入
@app.route("/member", methods=['GET'])
def member_page():
    if not session['SIGNED-IN']:
        return redirect('/')
    return render_template('login-success.html')

# 登入失敗
@app.route("/error")
def error_page():
    errorMessage = request.args.get('message','')
    return render_template('login-error.html', errorMessage = errorMessage)

# 計算正整數平方
@app.route("/square/<int:result>")
def square_result(result):
    result = (result ** 2)
    return render_template('square.html', result = result)

if __name__ == "__main__":
    app.run(port=3000)
