# 第三方扩展库，一般都引用app
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# 创建一个modles对象
mdb = SQLAlchemy()
# 创建迁移数据的对象
migrate = Migrate()


def init_ext(app):
    mdb.init_app(app=app)
    migrate.init_app(app, mdb)