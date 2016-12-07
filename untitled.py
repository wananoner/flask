from flask import Flask, flash, render_template, request

app = Flask(__name__)
app.secret_key = '123'

@app.route('/')
def hello_world():
    flash("Hello, my girl")
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    form = request.form
    username = form.get('username')
    password = form.get('password')

    if not username:
        flash("请输入用户名")
        return render_template("index.html")
    if not password:
        flash("请输入密码")
        return render_template("index.html")
    if username == 'wangbo' and password == '123456':
        flash("登陆成功")
        return render_template("index.html")
    else:
        flash("用户名或密码错误")
        return render_template("index.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run()
