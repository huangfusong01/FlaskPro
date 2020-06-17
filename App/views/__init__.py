'''
def init_route(app):

    @app.route("/Login")
    def login():
        name = 'hfs'
        return 'Hello Worrd %s' %name
'''
'''
1.创建蓝灯的作用是为了保证视图的管理
2.先去对应的views里头定义视图函数，通过new对象来构造执行__init__方法
3.蓝图注册后，可以通过蓝图找到路由的使用
'''
from .firse_blue import blue
from .seccond_blus import blue

"""
1.在应用对象上注册这个蓝图对象
2.blue 是定义的蓝图对象
3.通过懒加载的方式，先定义在注册
"""

def init_view(app):
    app.register_blueprint(blue)
