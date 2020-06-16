from flask_migrate import MigrateCommand
from flask_script import Manager
from App import creat_app

app = creat_app()
manage = Manager(app=app)

"""
manage常用命名
    *python manage.py 查看这个命名下的指令

manage数据迁移命名
    *python manage.py db init (实行数据迁移时第一次使用需要初始化)，执行完成后会生成迁移文件夹
    *python manage.py db migrate 生成迁移数据文件
    *python manage.py db upgrade 更新数据库
    
    
"""
# 往manage里头加入db命名
manage.add_command("db",MigrateCommand)

if __name__ == "__main__":
    manage.run()
