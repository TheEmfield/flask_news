from datetime import *
from . import db


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    news = db.relationship('News', back_populates='category')


    def _repr_(self):
        return f'Category {self.id}: ({self.title})'


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True, nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db. Foreignkey('category.id'), nullable=True)
    category = db.relationship('Category', back_populates='news')

    def _repr_(self):
        return f'News {self.id}: ({self.title[:20]}...)'