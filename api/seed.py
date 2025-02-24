from models import db, Question, Tutorial

def seed_data():
        if Tutorial.query.first() is None:
                tutorial1 = Tutorial(week=1, open=True, has_submission=False)
                tutorial2 = Tutorial(week=2, open=True, has_submission=False)
                tutorial3 = Tutorial(week=3, open=False, has_submission=False)
                db.session.add_all([tutorial1, tutorial2, tutorial3])
                db.session.commit()
        if Question.query.first() is None:
                barbara_example = Question(
                        tutorial_id=1,
                        premise1='All animals are mortals',
                        premise2='All humans are animals',
                        conclusion='All humans are mortals',
                        major_term='mortals',
                        minor_term='humans',
                        middle_term='animals',
                        valid=True
                )
                bocardo_example = Question(
                        tutorial_id=1,
                        premise1='Some cats are not ginger',
                        premise2='All cats are animals',
                        conclusion='Some animals are not ginger',
                        major_term='ginger',
                        minor_term='animals',
                        middle_term='cats',
                        valid=True
                )
                celarent_example = Question(
                        tutorial_id=2,
                        premise1='No rectangles are circles',
                        premise2='All squares are rectangles',
                        conclusion='No squares are circles',
                        major_term='circles',
                        minor_term='squares',
                        middle_term='rectangles',
                        valid=True
                )
                false_example_1 = Question(
                        tutorial_id=1,
                        premise1='Some fruit are yellow',
                        premise2='All bananas are fruit',
                        conclusion='All bananas are yellow',
                        major_term='yellow',
                        minor_term='bananas',
                        middle_term='fruit',
                        valid=False
                )
                db.session.add_all([barbara_example, bocardo_example, celarent_example, false_example_1])
                db.session.commit()

if __name__ == '__main__':
    seed_data()
