from App.ext import mdb


class User(mdb.Model):
    id = mdb.Column(mdb.Integer, primary_key=True)
    username = mdb.Column(mdb.String(16))

    def save(self):
        mdb.session.add(self)
        mdb.session.commit()
