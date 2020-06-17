from App.ext import mdb


class User(mdb.Model):
    id = mdb.Column(mdb.Integer, primary_key=True)
    username = mdb.Column(mdb.String(16))

    def save(self):
        mdb.session.add(self)
        mdb.session.commit()


class Teach(mdb.Model):

    id = mdb.Column(mdb.Integer,primary_key=True)
    teachername = mdb.Column(mdb.String(8),default='黄福送')

    def save(self):
        mdb.session.add(self)
        mdb.session.commit()
