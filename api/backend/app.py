import json
import utils.syllogism_checker as syllogism_checker
from flask import Flask, jsonify, request
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, Student, Question, Tutorial, Answer, Submission
from seed import seed_data

app = Flask(__name__, static_folder='../build', static_url_path='/')

#database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app) #cross origin resource sharing

migrate = Migrate(app, db)
db.init_app(app)

bcrypt = Bcrypt(app)
app.json.compact = False

@app.route('/api/tutorials', methods=['GET'])
def get_tutorials():
    tutorials = Tutorial.query.all()
    data_list = []
    for tutorial in tutorials:
        data = {}
        data["tutorial_id"] = tutorial.tutorial_id
        data["week"] = tutorial.week
        data_list.append(data)
    return jsonify({"tutorials": data_list})

@app.route('/api/questions', methods=['GET'])
def get_questions():
    tutorial_week = request.args.get('tutorial_week', default=1, type=int)
    questions = Question.query.filter_by(tutorial_id=tutorial_week).all()
    data_list = []
    for question in questions:
        data = {}
        data["question_id"] = question.question_id
        data["tutorial_id"] = question.tutorial_id
        data["premise1"] = question.premise1
        data["premise2"] = question.premise2
        data["conclusion"] = question.conclusion
        data["major_term"] = question.major_term
        data["minor_term"] = question.minor_term
        data["middle_term"] = question.middle_term
        data["valid"] = question.valid
        data_list.append(data)
    return jsonify({"questions": data_list})

#This endpoint is not called in current application, but would be used in future work on student authentication system
@app.route('/api/students', methods=['POST'])
def create_student():
    data = request.get_json()
    student_id = data['student_id']
    name = data['name']

    existing_student = Student.query.filter_by(student_id=student_id).first()
    if existing_student:
        return jsonify({'error': 'Student ID already exists'}), 400

    new_student = Student(student_id=student_id, name=name)
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student created!'})

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/check', methods=['POST'])
def check_answers():
    response = {}
    answers = []
    student_id = 1 #currently hardcoded, but if we implement a student authentication system, this will be replaced with the student's ID
    try:
        data = request.get_json()
        questions = data.get('questionStates', [])
        tutorial_id = data.get('tutorialId', -1)
        submission = Submission(
            student_id=student_id,
            tutorial_id=tutorial_id
        )
        db.session.add(submission)
        for question in questions:
            index = question.get('index', None)
            sectionStates = question.get('sectionStates', {})
            lineStates = question.get('lineStates', {})
            syllogism = question.get('syllogism', {})
            selectedAnswer = question.get('selectedAnswer', None)
            result = syllogism_checker.check_answer(sectionStates, lineStates, selectedAnswer, syllogism)
            response[index] = result
            new_answer = Answer(
                submission_id=1,
                question_id=index,
                answer=json.dumps({'sectionStates': sectionStates, 'lineStates': lineStates, 'selectedAnswer': selectedAnswer}),
                automarker_feedback=json.dumps({
                    'incorrect_sections': result['incorrect_sections'],
                    'incorrect_lines': result['incorrect_lines'],
                    'main_answer_correct': result['main_answer_correct']
                }),)
            answers.append(new_answer)
            db.session.add(new_answer)
        db.session.commit() #save to db
        return jsonify({
            'status': 'success',
            'result': response
        }), 200

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        seed_data()
        app.run(debug=True)




