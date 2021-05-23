from app import db
from sqlalchemy.sql import func
import enum


class CouponType(enum.Enum):
    AMOUNT = 1
    PERCENT = 2


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Coupon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    discount = db.Column(db.Float, nullable=False)
    code = db.Column(db.String(16), unique=True, nullable=False)
    type = db.Column(db.Enum(CouponType), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
