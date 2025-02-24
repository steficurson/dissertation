from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import CheckConstraint

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'

    student_id = db.Column(db.String(8), primary_key=True)
    name = db.Column(db.String, nullable=False)
    submissions = relationship('Submission', backref='student')

    def __repr__(self): #defines how the object is represented as a string
        return '<Item %r>' % self.name

class Question(db.Model):
    __tablename__ = 'questions'

    question_id = db.Column(db.Integer, index=True, primary_key=True)
    tutorial_id = db.Column(db.Integer, db.ForeignKey('tutorials.tutorial_id'), nullable=False)
    premise1 = db.Column(db.String(100), nullable=False)
    premise2 = db.Column(db.String(100), nullable=False)
    conclusion = db.Column(db.String(100), nullable=False)
    major_term = db.Column(db.String(50), nullable=False)
    minor_term = db.Column(db.String(50), nullable=False)
    middle_term = db.Column(db.String(50), nullable=False)
    valid = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<Item %r>' % self.question_id

class Tutorial(db.Model):
    __tablename__ = 'tutorials'

    tutorial_id = db.Column(db.Integer, index=True, primary_key=True)
    week = db.Column(db.Integer, nullable=False, unique=True)
    open = db.Column(db.Boolean, nullable=False, unique=False)
    has_submission = db.Column(db.Boolean, nullable=False, unique=False)
    questions = relationship('Question', backref='tutorial')

    __table_args__ = (
        CheckConstraint('week > 0', name='check_week_positive'),
        CheckConstraint('week < 12', name='check_week_less_than_12')
    )

    def __repr__(self):
        return '<Item %r>' % self.tutorial_id

class Answer(db.Model):
    __tablename__ = 'answers'

    answer_id = db.Column(db.Integer, index=True, primary_key=True)
    submission_id = db.Column(db.Integer, db.ForeignKey('submissions.submission_id'), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'), primary_key=True)
    answer = db.Column(db.String(500), nullable=False)
    correct = db.Column(db.Boolean)

    def __repr__(self):
        return '<Item %r>' % self.question_id

class Submission(db.Model):
    __tablename__ = 'submissions'

    submission_id = db.Column(db.Integer, index=True, primary_key=True)
    student_id = db.Column(db.String(8), db.ForeignKey('students.student_id'), primary_key=True)
    tutorial_id = db.Column(db.Integer, db.ForeignKey('tutorials.tutorial_id'), primary_key=True)
    answers = relationship('Answer', backref='submission')

    def __repr__(self):
        return '<Item %r>' % self.student_id
