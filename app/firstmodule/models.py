from app import db


class HoroscopeModel(db.Model):
    __tablename__ = 'horoscope'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return "<HoroscopeModel %r>" % self.id
