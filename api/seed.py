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
                        premise1='All animals are mortals',
                        premise2='All humans are animals',
                        conclusion='All humans are mortals',
                        major_term='mortals',
                        minor_term='humans',
                        middle_term='animals',
                        valid=True
                )
                bocardo_example = Syllogism(
                        tutorial_id=1,
                        premise1='Some cats are not ginger',
                        premise2='All cats are animals',
                        conclusion='Some animals are not ginger',
                        major_term='ginger',
                        minor_term='animals',
                        middle_term='cats',
                        valid=True
                )
                celarent_example = Syllogism(
                        tutorial_id=1,
                        premise1='No rectangles are circles',
                        premise2='All squares are rectangles',
                        conclusion='No squares are circles',
                        major_term='circles',
                        minor_term='squares',
                        middle_term='rectangles',
                        valid=True
                )
                db.session.add_all([barbara_example, bocardo_example, celarent_example])
                db.session.commit()

if __name__ == '__main__':
    seed_data()
