from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import CheckConstraint

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'

    student_id = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self): #defines how the object is represented as a string
        return '<Item %r>' % self.name

class Syllogism(db.Model):
    __tablename__ = 'syllogisms'

    syllogism_id = db.Column(db.Integer, index=True, primary_key=True)
    tutorial_id = db.Column(db.Integer, db.ForeignKey('tutorials.tutorial_id'), nullable=False)
    premise1 = db.Column(db.String(100), nullable=False)
    premise2 = db.Column(db.String(100), nullable=False)
    conclusion = db.Column(db.String(100), nullable=False)
    major_term = db.Column(db.String(50), nullable=False)
    minor_term = db.Column(db.String(50), nullable=False)
    middle_term = db.Column(db.String(50), nullable=False)
    valid = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<Item %r>' % self.syllogism_id

class Tutorial(db.Model):
    __tablename__ = 'tutorials'

    tutorial_id = db.Column(db.Integer, index=True, primary_key=True)
    week = db.Column(db.Integer, nullable=False, unique=True)
    syllogisms = relationship('Syllogism', backref='tutorial')

    __table_args__ = (
        CheckConstraint('week > 0', name='check_week_positive'),
        CheckConstraint('week < 12', name='check_week_less_than_12')
    )

    def __repr__(self):
        return '<Item %r>' % self.tutorial_id
