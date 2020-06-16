# 配置数据库url信息，返回一个连接格式
def get_db_url(dbinfo):

    engine = dbinfo.get("ENGING") or "sqlite"
    driver = dbinfo.get("DRIVER") or "sqlite"
    user = dbinfo.get("USER") or ""
    paw = dbinfo.get("PWD") or ""
    host = dbinfo.get("HOST") or ""
    port = dbinfo.get("PORT") or ""
    name = dbinfo.get("NAME") or "sqlite.db"

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, paw, host, port, name)


class Config():
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


# 开发环境，可以通过这样的方式来配置多个环境
class DevelopConfing(Config):
    DEBUG = True

    dbinfo = {

        "ENGING": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PWD": "HFS123456",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "GPI"
    }
    SQLALCHEMY_DATABASE_URL = get_db_url(dbinfo)


# 测试环境
class TestConfing(Config):
    DEBUG = True

    dbinfo = {

        "ENGING": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PWD": "123456",
        "HOST": "139.9.179.188",
        "PORT": "3306",
        "NAME": "Test"
    }
    SQLALCHEMY_DATABASE_URL = get_db_url(dbinfo)


# 把上面的环境封装一个字典，通过获取字典的key来加载环境
envs = {
    "developConfing": "DevelopConfing",
    "testConfing": "TestConfing"
}

#print(envs.get("testConfing"))

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

if __name__ == '__main__':
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = TestConfing.SQLALCHEMY_DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db = SQLAlchemy(app)
    db.create_all()