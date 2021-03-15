from flask import Flask, render_template
from flask import request #載入 Requests 物件
import json
from flask import session #載入session
from flask import redirect # 載入redirect
import os
from datetime import timedelta

# Establish Application 物件, 可以設定靜態檔案的路徑
app = Flask(
        __name__,
        static_folder ="public", #靜態檔案的資料夾名稱, 預設:static
        static_url_path = "/" #靜態檔案對應的網址路徑, 預設:/static
            )

app.config['SECRET_KEY'] = os.urandom(24) #用os 隨機生成24位密鑰
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days = 30) #過期為30天

#建立網站首頁的回應方式
@app.route("/")
def index(): #用來回應網站首頁的function

    #Request
    # print("請求方法：", request.method)
    # print("通訊協定：", request.scheme)
    # print("主機名稱：", request.host)
    # print("路徑：", request.path)
    # print("完整網址：", request.url)

    #Headers
    # print("瀏覽器＆作業系統：", request.headers.get("user-agent"))
    # print("語言偏好：", request.headers.get("accept-language"))
    # print("引薦網址(點過來的網站)：", request.headers.get("referrer"))

    # #用user language preference to set greetings
    # lang = request.headers.get("accept-language")
    # if lang.startswith("en"):
    #     return "Hi, English!"
    # else:
    #     return "嗨, 中文"

    # return "Hello, World!" #回應網站首頁內容

    #如果session 存在, 進到member頁面 or 回到首頁登入頁
    if session.get('username') != None and session.get('role') != None:
        return redirect('/member')
    else:
        return render_template('index.html')

# #建立路徑 /getSum 對應的處理函式
# #利用要求字串(Query String) 提供彈性  /getSum?max=最大數字&min=最小數字
# @app.route("/getSum")
# def getSum():
#     max_number = request.args.get("max", 100) # 100 = 預設值
#     max_number = int(max_number) # !!!! 記得轉換成數字
#     min_number = request.args.get("min", 0)  # 100 = 預設值
#     min_number = int(min_number)  # !!!! 記得轉換成數字
#     total_sum = 0
#     # total_sum = (min_number + max_number) * (max_number-min_number) / 2 #min_number >= 1
#     for i in range(min_number,max_number+1):
#         total_sum += i
#
#     return f"結果：{total_sum}"

# #建立路徑 /signin 對應的處理函式
# #利用要求字串(Query String) 提供彈性  /signin?account=帳號&password=密碼
# 設置session
@app.route("/signin", methods = ["POST"])
def signin():
    #接收前端的POST表單字串
    account = request.form["account"]
    password = request.form["password"]
    #設置session
    session['username'] = account
    session['role'] = password
    if account == "test" and password == "test":
        session.permanent = True #過期為30天
        return redirect("/member")
    else:
        session['username'] = None #刪除session
        session['role'] = None  # 刪除session
        return redirect("/error")

#member route
@app.route("/member/")
def member():
    # 如果session 存在, 進到member頁面 or 回到首頁登入頁
    if session.get('username') != None and session.get('role') != None:
        # print(session.get('username'), session.get('role'))
        return render_template('member.html')
    else:
        return redirect('/')

#error route
@app.route("/error/")
def error():
    return render_template('error.html')

@app.route("/logout")
def logout():
    session['username'] = None  # 刪除session
    session['role'] = None  # 刪除session
    return redirect("/")


# #靜態路由 / 對應的處理函式
# @app.route("/hello/")
# def hello():
#     # return json string
#     # return json.dumps({
#     #     "status":"OK",
#     #     "text":"你好!"
#     # }, ensure_ascii=False) # 不要用ascii 處理中文
#     # redirect to google
#     return redirect("https://www.google.com/")
# #動態路由
# @app.route("/data/<user>")
# def getData(user):
#     return f"DATA! {user}"

# 啟動伺服器, 可透過port 參數 指定
app.run(port=3000)