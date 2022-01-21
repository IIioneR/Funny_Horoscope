from flask import request, redirect, render_template, Blueprint
from sqlalchemy import func

from app import db
from app.module.models import HoroscopeModel

api_route = Blueprint('api', __name__, url_prefix='/api')


@api_route.route('/', methods=['GET'])
def get_horoscope():
    horoscope_info = HoroscopeModel.query.order_by(func.random()).first()
    return render_template('horoscope/get_horoscope_info.html', horoscope_info=horoscope_info)


@api_route.route('/', methods=['POST'])
def create_horoscope():

    text = request.form['text']
    horoscope = HoroscopeModel(text=text)
    try:
        db.session.add(horoscope)
        db.session.commit()
        return render_template('horoscope/success_created.html')
    except:
        return 'Не получилось создать гороскоп :('


@api_route.route('/<int:id>/u', methods=['GET', 'POST'])
def update_horoscope(id):
    horoscope = HoroscopeModel.query.get(id)
    if request.method == 'POST':
        horoscope.text = request.form['text']

        try:
            db.session.commit()
            return render_template('horoscope/success_updated.html')
        except:
            return 'Не получилось отредактировать гороскоп :('
    else:
        return render_template('horoscope/horoscope_update.html', horoscope=horoscope)


@api_route.route('/<int:id>/d')
def delete_horoscope(id):
    horoscope = HoroscopeModel.query.get_or_404(id)

    try:
        db.session.delete(horoscope)
        db.session.commit()
        return render_template('horoscope/success_deleted.html')
    except:
        return 'Не удалось удалить гороскоп'
