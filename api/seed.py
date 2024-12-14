from models import db, Syllogism, Tutorial
from app import app

def seed_data():
    with app.app_context():
        if Tutorial.query.first() is None:
                tutorial1 = Tutorial(week=1)
                tutorial2 = Tutorial(week=2)
                db.session.add_all([tutorial1, tutorial2])
                db.session.commit()
        if Syllogism.query.first() is None:
                barbara_example = Syllogism(
                        tutorial_id=1,
                        premise1='All humans are animals',
                        premise2='All animals are mortal',
                        conclusion='All humans are mortal',
                        valid=True
                )
                bocardo_example = Syllogism(
                        tutorial_id=1,
                        premise1='Some cats do not have tails',
                        premise2='All cats are animals',
                        conclusion='Some animals do not have tails',
                        valid=True
                )
                camestres_example = Syllogism(
                        tutorial_id=1,
                        premise1='All squares are rectangles',
                        premise2='No rectangles are circles',
                        conclusion='No squares are circles',
                        valid=True
                )
                db.session.add_all([barbara_example, bocardo_example, camestres_example])
                db.session.commit()

if __name__ == '__main__':
    seed_data()
