# 第三方扩展库，一般都是引用app


def init_ext(app):
    pass


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
class DevelopConfing():
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
class TestConfing():
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


# 把上面的环境封装一个字典，通过获取字典的key来加载环境
envs = {
    "developConfing": "DevelopConfing",
    "testConfing": "TestConfing"
}