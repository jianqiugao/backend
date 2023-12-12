from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required

app = Flask(__name__, static_folder='./templates')
app.config['SECRET_KEY'] = '80aa2026d1717a85ad0b94d19ad4adfb551b11577e0197ec00b9b2c34b13c9ad'  # 设置一个随机的密钥
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

    def is_active(self):
        # Implement your logic here to determine if the user is active
        return True  # Change this based on your requirements

    def get_id(self):
        return str(self.id)  # Convert user ID to a string


# 假设这是你的用户数据库
users = {
    'alice': 'password123',
    'bob': 'secret456'
}


@login_manager.user_loader
def load_user(user_id):
    # 根据用户 ID 加载用户对象
    return users.get(user_id)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = users.get(username) # 拿到一个字符串
    user = User(username)

    if username in users and users[username] == password:
        login_user(user, remember=True)
        flash("登录成功！", "success")
        # 登录成功，可以跳转到其他页面
        return redirect(url_for('dashboard'))
    else:
        return "Invalid credentials. Please try again."


@app.route('/dashboard')
@login_required
def dashboard():
    return "Welcome to the dashboard!"


if __name__ == '__main__':
    app.run(debug=True)
