import unittest

from syllogism_checker import check_answer
from test_constants import valid_syllogisms, invalid_syllogisms

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
        result = check_answer(sectionStates, lineStates, valid_syllogisms["barbara"])
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
        result = check_answer(sectionStates, lineStates, valid_syllogisms["celarent"])
        self.assertEqual(result, True)

    def test_check_answer_camestres_should_return_true(self):
        sectionStates = {
            "A":{"state":"default"},
            "B":{"state":"selected"},
            "C":{"state":"default"},
            "AB":{"state":"default"},
            "AC":{"state":"selected"},
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
        result = check_answer(sectionStates, lineStates, valid_syllogisms["camestres"])
        self.assertEqual(result, True)

    def test_check_answer_darii_should_return_true(self):
        sectionStates = {
            "A":{"state":"selected"},
            "B":{"state":"default"},
            "C":{"state":"default"},
            "AB":{"state":"default"},
            "AC":{"state":"selected"},
            "BC":{"state":"default"},
            "ABC":{"state":"crossed"}
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
        result = check_answer(sectionStates, lineStates, valid_syllogisms["darii"])
        self.assertEqual(result, True)

    def test_check_answer_disamis_should_return_true(self):
        sectionStates = {
            "A":{"state":"selected"},
            "B":{"state":"default"},
            "C":{"state":"default"},
            "AB":{"state":"selected"},
            "AC":{"state":"default"},
            "BC":{"state":"default"},
            "ABC":{"state":"crossed"}
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
        result = check_answer(sectionStates, lineStates, valid_syllogisms["disamis"])
        self.assertEqual(result, True)

    def test_check_answer_ferio_should_return_true(self):
        sectionStates = {
            "A":{"state":"default"},
            "B":{"state":"default"},
            "C":{"state":"default"},
            "AB":{"state":"selected"},
            "AC":{"state":"crossed"},
            "BC":{"state":"default"},
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
        result = check_answer(sectionStates, lineStates, valid_syllogisms["ferio"])
        self.assertEqual(result, True)

    def test_check_answer_baroco_should_return_true(self):
        sectionStates = {
            "A":{"state":"default"},
            "B":{"state":"selected"},
            "C":{"state":"crossed"},
            "AB":{"state":"default"},
            "AC":{"state":"default"},
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
        result = check_answer(sectionStates, lineStates, valid_syllogisms["baroco"])
        self.assertEqual(result, True)

    def test_check_answer_bocardo_should_return_true(self):
        sectionStates = {
            "A":{"state":"selected"},
            "B":{"state":"default"},
            "C":{"state":"default"},
            "AB":{"state":"selected"},
            "AC":{"state":"crossed"},
            "BC":{"state":"default"},
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
        result = check_answer(sectionStates, lineStates, valid_syllogisms["bocardo"])
        self.assertEqual(result, True)

    # def test_check_answer_barbera_should_return_false(self):
    #     sectionStates = {
    #         "A":{"state":"selected"},
    #         "B":{"state":"default"},
    #         "C":{"state":"default"},
    #         "AB":{"state":"default"},
    #         "AC":{"state":"selected"},
    #         "BC":{"state":"default"},
    #         "ABC":{"state":"selected"}
    #     }
    #     lineStates = {
    #         "AB_ABC":{"state":"default"},
    #         "AC_ABC":{"state":"default"},
    #         "BC_ABC":{"state":"default"},
    #         "A_AB":{"state":"default"},
    #         "B_AB":{"state":"default"},
    #         "A_AC":{"state":"default"},
    #         "C_AC":{"state":"default"},
    #         "B_BC":{"state":"default"},
    #         "C_BC":{"state":"default"}
    #     }
    #     result = check_answer(sectionStates, lineStates, invalid_syllogisms["barbera"])
    #     self.assertEqual(result, False)

    # def test_check_answer_barberi_should_return_false(self):
    #     sectionStates = {
    #         "A":{"state":"selected"},
    #         "B":{"state":"default"},
    #         "C":{"state":"default"},
    #         "AB":{"state":"default"},
    #         "AC":{"state":"selected"},
    #         "BC":{"state":"default"},
    #         "ABC":{"state":"selected"}
    #     }
    #     lineStates = {
    #         "AB_ABC":{"state":"default"},
    #         "AC_ABC":{"state":"default"},
    #         "BC_ABC":{"state":"default"},
    #         "A_AB":{"state":"default"},
    #         "B_AB":{"state":"default"},
    #         "A_AC":{"state":"default"},
    #         "C_AC":{"state":"default"},
    #         "B_BC":{"state":"default"},
    #         "C_BC":{"state":"default"}
    #     }
    #     result = check_answer(sectionStates, lineStates, invalid_syllogisms["barberi"])
    #     self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
