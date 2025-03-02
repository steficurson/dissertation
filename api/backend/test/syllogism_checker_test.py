import unittest

from utils.syllogism_checker import check_answer

class TestSyllogismChecker(unittest.TestCase):
    def test_check_answer_barbara_should_return_true(self):
        sectionStates = {
            "A":{"state":"selected"},
            "B":{"state":"default"},
            "C":{"state":"selected"},
            "AB":{"state":"default"},
            "AC":{"state":"selected"},
            "BC":{"state":"selected"},
            "ABC":{"state":"default"}
        }
        lineStates = {
            "AB_ABC":{"state":"default"},
            "AC_ABC":{"state":"default"},
            "BC_ABC":{"state":"default"},
            "A_AB":{"state":"default"},
            "B_AB":{"state":"default"},
            "A_AC":{"state":"default"},
            "C_AC":{"state":"default"},
            "B_BC":{"state":"default"},
            "C_BC":{"state":"default"}
        }
        barbara = {
            "conclusion":"All humans are mortals",
            "major_term":"mortals",
            "middle_term":"animals",
            "minor_term":"humans",
            "premise1":"All animals are mortals",
            "premise2":"All humans are animals",
            "question_id":1,
            "tutorial_id":1,
            "valid":True
        }
        result = check_answer(sectionStates, lineStates, barbara)
        self.assertEqual(result, True)

    def test_check_answer_celarent_should_return_true(self):
        sectionStates = {
            "A":{"state":"default"},
            "B":{"state":"default"},
            "C":{"state":"selected"},
            "AB":{"state":"selected"},
            "AC":{"state":"default"},
            "BC":{"state":"selected"},
            "ABC":{"state":"selected"}
        }
        lineStates = {
            "AB_ABC":{"state":"default"},
            "AC_ABC":{"state":"default"},
            "BC_ABC":{"state":"default"},
            "A_AB":{"state":"default"},
            "B_AB":{"state":"default"},
            "A_AC":{"state":"default"},
            "C_AC":{"state":"default"},
            "B_BC":{"state":"default"},
            "C_BC":{"state":"default"}
        }
        celarent = {
            "conclusion": "No S are P",
            "major_term": "P",
            "middle_term": "M",
            "minor_term": "S",
            "premise1": "No M are P",
            "premise2": "All S are M",
            "question_id":2,
            "tutorial_id":1,
            "valid":True
        }
        result = check_answer(sectionStates, lineStates, celarent)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()
