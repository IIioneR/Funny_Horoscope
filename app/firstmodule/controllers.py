from flask import request, redirect, render_template, Blueprint
from sqlalchemy import func

from app import db
from app.firstmodule.models import HoroscopeModel

module = Blueprint('horoscope', __name__, url_prefix='/')


@module.route('/create-horoscope', methods=['GET', 'POST'])
def create_horoscope():
    if request.method == 'POST':
        text = request.form['text']

        horoscope = HoroscopeModel(text=text)

        try:
            db.session.add(horoscope)
            db.session.commit()
            return redirect('/succes-creating')
        except:
            return 'Не получилось создать гороскоп :('
    else:
        return render_template('horoscope/create_horoscope.html')


@module.route('/succes-creating')
def succes_creating():  # put application's code here
    return render_template('horoscope/succes_created.html')


@module.route('/get-horoscope', methods=['GET', 'POST'])
def get_horoscope():
    if request.method == 'POST':
        horoscope_info = HoroscopeModel.query.order_by(func.random()).first()
        return render_template('horoscope/horoscope.html', horoscope_info=horoscope_info)
    return render_template('horoscope/get_horoscope.html')


@module.route('/horoscope-list')
def get_goroscopes_list():
    horoscope_list = HoroscopeModel.query.order_by(HoroscopeModel.id).all()
    return render_template('horoscope/horoscope_list.html', horoscope_list=horoscope_list)


@module.route('/horoscope/<int:id>/delete')
def delete_horoscope(id):
    horoscope = HoroscopeModel.query.get_or_404(id)

    try:
        db.session.delete(horoscope)
        db.session.commit()
        return redirect('/horoscope-list')
    except:
        return 'Не удалось удалить гороскоп'


@module.route('/horoscope/<int:id>/update', methods=['GET', 'POST'])
def update_horoscope(id):
    horoscope = HoroscopeModel.query.get(id)
    if request.method == 'POST':
        horoscope.text = request.form['text']

        try:
            db.session.commit()
            return redirect('/horoscope-list')
        except:
            return 'Не получилось отредактировать гороскоп :('
    else:
        return render_template('horoscope/horoscope_update.html', horoscope=horoscope)
