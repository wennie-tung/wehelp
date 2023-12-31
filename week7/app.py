from flask import Flask, render_template, redirect, request, session, jsonify
app = Flask(__name__, static_folder="public", static_url_path="/")

# Session 密鑰
app.secret_key = "SecretKey20230807"

# MySQL
import mysql.connector
# 連接到本機的 MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="website"
)

mycursor = mydb.cursor()

# Home Page
@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

# Sign Up
@app.route("/signup", methods=['POST'])
def signup():
    input_name = request.form.get('r_name')
    input_username = request.form.get('r_username')
    input_password = request.form.get('r_password')
    sql = 'SELECT * FROM member WHERE username = %s'
    mycursor.execute(sql, (input_username,))
    existing_username = mycursor.fetchall()

    if existing_username:
        register_errorMSG = "The account has already been registered."
        return redirect('/error?message=' + register_errorMSG)
    else:
        registerSuccessMsg = "Registration successful! Please log in again."
        sql = 'INSERT INTO member (name, username, password) VALUES (%s, %s, %s)'
        val = (input_name, input_username, input_password)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect('/?message=' + registerSuccessMsg)

# Sign In
@app.route("/signin", methods=['POST'])
def signin():
    loginUsername = request.form.get('l_username')
    loginPassword = request.form.get('l_password')
    sql = 'SELECT * FROM member WHERE username = %s AND password = %s'
    mycursor.execute(sql, (loginUsername,loginPassword))
    isMember = mycursor.fetchall()
    print(isMember)

    if isMember:
        session['SIGN-IN'] = True
        session['ID'] = isMember[0][0]
        session['name'] = isMember[0][1]
        session['username'] = isMember[0][2]
        return redirect('/member')
    else:
        loginErrorMsg = "Incorrect username or password."
        return redirect('/error?message=' + loginErrorMsg)

# Sign Out
@app.route("/signout", methods=['GET'])
def signout():
    session['SIGN-IN'] = False
    return redirect('/')

# 成功登入 : member page
@app.route("/member", methods=['GET'])
def loginsuccess():
    # 如果不是登入狀態，即導回首頁
    if not session['SIGN-IN']:
        return redirect('/')
    # 登入狀態
    name = session['name']
    memberID = session['ID']
    sql = 'SELECT member.name, message.content, message.id, member.id FROM member INNER JOIN message ON member.id = message.member_id'
    mycursor.execute(sql)
    messageData = mycursor.fetchall()
    messageContent = messageData
    return render_template("member-page.html", name = name, messageContent = messageContent, memberID = memberID)

# 登入失敗
@app.route("/error", methods=['GET'])
def error_page():
    errorMessage = request.args.get('message','')
    return render_template('login-failed.html', errorMessage = errorMessage)

# 留言功能
@app.route("/createMessage", methods=['POST'])
def createMessage():
    # 將留言內容紀錄到 message 資料
    memberID = session['ID']
    memberMessage = request.form.get("guestMessage")
    sql = 'INSERT INTO message (member_id, content) VALUES (%s, %s)'
    val = (memberID, memberMessage)
    mycursor.execute(sql, val)
    mydb.commit()
    return redirect('/member')

# 刪除留言功能 (Optional)
@app.route("/deleteMessage/<int:messageID>", methods=['POST'])
def deleteMessage(messageID):
    sql = 'DELETE FROM message WHERE id = %s'
    val = (messageID,)
    mycursor.execute(sql, val)
    mydb.commit()
    return redirect('/member')

# 查詢會員資料 API
@app.route("/api/member", methods=['GET'])
def getMember():
    username = request.args.get("username")
    mycursor = mydb.cursor(dictionary=True)
    sql = 'SELECT id, name, username FROM member WHERE username = %s'
    mycursor.execute(sql, (username,))
    searchResult = mycursor.fetchone()
    if searchResult:
        response_data = {"data" : searchResult}
    else:
        response_data = {"data": None}
    return jsonify(response_data)

# 更新姓名
@app.route("/api/member", methods=['PATCH'])
def updateName():
    try:
        # 解析請求的 JSON 資料
        requestData = request.get_json()
        print(requestData)
        if 'name' in requestData:
            newName = requestData['name']
            username = session['username']
            sql = 'UPDATE member SET name = %s WHERE username= %s'
            val = (newName, username,)
            mycursor.execute(sql, val)
            mydb.commit()
            session['name'] = newName
            return jsonify({"ok":True, "name":newName})
        else:
            return jsonify({"error":True})
        
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(port=3000)