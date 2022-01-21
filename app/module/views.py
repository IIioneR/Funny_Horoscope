from flask import request, redirect, render_template, Blueprint
from sqlalchemy import func

from app import db
from app.module.models import HoroscopeModel

views = Blueprint('horoscope', __name__, url_prefix='/horoscope')


@views.route('/new')
def creating_horoscope():
    return render_template('horoscope/creating_horoscope.html')


@views.route('/horoscope-list')
def getting_horoscope_list():
    horoscope_list = HoroscopeModel.query.order_by(HoroscopeModel.id).all()
    return render_template('horoscope/horoscope_list.html', horoscope_list=horoscope_list)


@views.route('/horoscope')
def getting_horoscope():
    return render_template('horoscope/get_horoscope.html')


