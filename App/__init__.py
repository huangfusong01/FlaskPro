from flask import Flask
from App.ext import init_ext
from App.settings import envs
from App.views import blue, init_view
import templates

def creat_app():
    #传项目的路径就是为了找模板的
    app = Flask(__name__,template_folder=r"E:\pyCharm\FlaskPro\templates",root_path=r'E:\pyCharm\FlaskPro')

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sqlite.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 所有通过懒加载的，在这个入口传对象来注册

    #app.config.from_object(envs.get("developConfing"))
    init_view(app)
    init_ext(app)
    #app.register_blueprint(blue)
    return app

