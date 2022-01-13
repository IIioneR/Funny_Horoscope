from flask import Flask, render_template, request, redirect

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///horoscope.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class HoroscopeModel(db.Model):
    __tablename__ = 'horoscope'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return "<HoroscopeModel %r>" % self.id


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/create-horoscope', methods=['GET', 'POST'])
def create_horoscope():
    if request.method == 'POST':
        text = request.form['text']

        horoscope = HoroscopeModel(text=text)

        try:
            db.session.add(horoscope)
            db.session.commit()
            return redirect('/succes-creating')
        except:
            'Не получилось создать гороскоп :('
    else:
        return render_template('create_horoscope.html')


@app.route('/succes-creating')
def succes_creating():  # put application's code here
    return render_template('succes_created.html')


@app.route('/get-horoscope', methods=['GET', 'POST'])
def get_horoscope():
    if request.method == 'POST':
        horoscope_info = HoroscopeModel.query.order_by(func.random()).first()
        return render_template('horoscope.html', horoscope_info=horoscope_info)
    return render_template('get_horoscope.html')


if __name__ == '__main__':
    app.run()
