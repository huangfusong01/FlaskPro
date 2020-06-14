from flask import Blueprint, redirect, url_for, render_template, make_response
from App.models import mdb, User


# 创建一个蓝图对象，可以根据这个名字来找到这个蓝图对象
blue = Blueprint('index', __name__)


# 在这个蓝图对象上进行操作,注册路由,指定静态文件夹,注册模版过滤器
@blue.route('/home')
def index():
    return "我是蓝图的首页"


@blue.route('/credtdb/')
def credtdb():
    mdb.create_all()
    return '创建成功'


@blue.route('/adduser/')
def add_user():
    user = User()
    user.username = 'tom12'
    user.save()
    #mdb.session.add(user)
    #mdb.session.commit()

    return "创建成功"

@blue.route('/selectusername/')
def select_user_name():
    usenname = User.query.get(1)
    Username = str(usenname)
    print('查询成功%s'%Username)
    return  '查询成功%s'%Username


'''
1.动态路由教程
2.地址：http://www.360doc.com/content/19/0626/14/12906439_844963679.shtml/

'''
@blue.route('/getid/<string:id>/')
def get_id(id):
    print(id)
    print(type(id))
    return id


@blue.route('/getIntNumber/<int:number>/')
def get_int_number(number):
    print(number)
    print(type(number))

    return str(number)


@blue.route('/getAngy/<any(a,b):tom>/')
def get_any(tom):
    print(tom)
    return tom


'''
1.路由反向解析
'''
@blue.route('/redirect/')
def getredirect():
    # url_for 第一个参数传的是蓝图的名称，也就是上面蓝图定义的传的
    #return redirect('/home')
    return redirect(url_for('index.index'))


@blue.route('/getresponst/',methods = ['get'])
def get_response():

    #response = make_response("<h2>cscscs</h2>")
    #return response
    return render_template('index.html')



