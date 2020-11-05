from flask import Flask,render_template
app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:michael88@127.0.0.1:3306/zqwz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'michaeljackson'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
from App.Views.TeacherView import teacher
app.register_blueprint(teacher, url_prefix='/teacher')

@app.route("/")
def hello():
    return render_template("login.html")

# 错误处理 404错误
@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html'), 404


# 错误处理 500错误
@app.errorhandler(500)
def serverError(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="8088")

