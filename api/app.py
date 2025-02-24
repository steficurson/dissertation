import time
import syllogism_checker
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

#with app.app_context():
#    db.create_all()
#    populate_tables(db)

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/api/day')
def get_current_day():
    return {'day': time.strftime('%A')}

@app.route('/api/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    data_list = []
    for student in students:
        data = {}
        data["student_id"] = student.student_id
        data["name"] = student.name
        data_list.append(data)
    return jsonify({"students": data_list}) #figure this out next

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

@app.route('/api/students', methods=['POST'])
def create_student():
    data = request.get_json()
    student_id = data['student_id']
    name = data['name']
    #validation stuff

    new_student = Student(student_id=student_id, name=name)
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'message': 'Student created!'})

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/check', methods=['POST'])
def check_endpoint():
    try:
        data = request.get_json()
        sectionStates = data.get('sectionStates', {})
        lineStates = data.get('lineStates', {})
        syllogism = data.get('syllogism', {})

        result = syllogism_checker.check_answer(sectionStates, lineStates, syllogism)

        return jsonify({
            'status': 'success',
            'result': result
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




