import unittest

from utils.syllogism_checker import check_answer
from utils.test_constants import valid_syllogisms, invalid_syllogisms

class TestSyllogismChecker(unittest.TestCase):
    def is_correct(self, result):
        return result["main_answer_correct"] and len(result["incorrect_sections"]) == 0 and len(result["incorrect_lines"]) == 0

    # Valid syllogisms completed correctly (covers every valid syllogism)
    def test_check_answer_barbara_correct_valid_should_return_true(self):
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
        result = check_answer(sectionStates, lineStates, True, valid_syllogisms["barbara"])
        self.assertEqual(self.is_correct(result), True)

    def test_check_answer_celarent_correct_valid_should_return_true(self):
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
        result = check_answer(sectionStates, lineStates, True, valid_syllogisms["celarent"])
        self.assertEqual(self.is_correct(result), True)

    def test_check_answer_camestres_correct_valid_should_return_true(self):
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
        result = check_answer(sectionStates, lineStates, True, valid_syllogisms["camestres"])
        self.assertEqual(self.is_correct(result), True)

    def test_check_answer_darii_correct_valid_should_return_true(self):
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
        result = check_answer(sectionStates, lineStates, True, valid_syllogisms["darii"])
        self.assertEqual(self.is_correct(result), True)

    def test_check_answer_disamis_correct_valid_should_return_true(self):
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
        result = check_answer(sectionStates, lineStates, True, valid_syllogisms["disamis"])
        self.assertEqual(self.is_correct(result), True)

    def test_check_answer_ferio_correct_valid_should_return_true(self):
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
        result = check_answer(sectionStates, lineStates, True, valid_syllogisms["ferio"])
        self.assertEqual(self.is_correct(result), True)

    def test_check_answer_baroco_correct_valid_should_return_true(self):
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
        result = check_answer(sectionStates, lineStates, True, valid_syllogisms["baroco"])
        self.assertEqual(self.is_correct(result), True)

    def test_check_answer_bocardo_correct_valid_should_return_true(self):
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
        result = check_answer(sectionStates, lineStates, True, valid_syllogisms["bocardo"])
        self.assertEqual(self.is_correct(result), True)

    def test_check_answer_datisi_correct_valid_should_return_true(self):
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
        result = check_answer(sectionStates, lineStates, True, valid_syllogisms["datisi"])
        self.assertEqual(self.is_correct(result), True)

    def test_check_answer_dimaris_correct_valid_should_return_true(self):
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
        result = check_answer(sectionStates, lineStates, True, valid_syllogisms["dimaris"])
        self.assertEqual(self.is_correct(result), True)

    def test_check_answer_cesare_correct_valid_should_return_true(self):
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
        result = check_answer(sectionStates, lineStates, True, valid_syllogisms["cesare"])
        self.assertEqual(self.is_correct(result), True)

    def test_check_answer_camenes_correct_valid_should_return_true(self):
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
        result = check_answer(sectionStates, lineStates, True, valid_syllogisms["camenes"])
        self.assertEqual(self.is_correct(result), True)

    def test_check_answer_festino_correct_valid_should_return_true(self):
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
        result = check_answer(sectionStates, lineStates, True, valid_syllogisms["festino"])
        self.assertEqual(self.is_correct(result), True)

    def test_check_answer_ferison_correct_valid_should_return_true(self):
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
        result = check_answer(sectionStates, lineStates, True, valid_syllogisms["ferison"])
        self.assertEqual(self.is_correct(result), True)

    def test_check_answer_fresison_correct_valid_should_return_true(self):
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
        result = check_answer(sectionStates, lineStates, True, valid_syllogisms["fresison"])
        self.assertEqual(self.is_correct(result), True)

    # Invalid syllogisms completed correctly
    def test_check_answer_barbera_correct_invalid_should_return_true(self):
        sectionStates = {
            "A":{"state":"selected"},
            "B":{"state":"default"},
            "C":{"state":"default"},
            "AB":{"state":"default"},
            "AC":{"state":"selected"},
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
        result = check_answer(sectionStates, lineStates, False, invalid_syllogisms["barbera"])
        self.assertEqual(self.is_correct(result), True)

    def test_check_answer_barberi_invalid_should_return_true(self):
        sectionStates = {
            "A":{"state":"selected"},
            "B":{"state":"default"},
            "C":{"state":"default"},
            "AB":{"state":"default"},
            "AC":{"state":"selected"},
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
        result = check_answer(sectionStates, lineStates, False, invalid_syllogisms["barberi"])
        self.assertEqual(self.is_correct(result), True)

    def test_check_answer_cemostros_invalid_should_return_true(self):
        sectionStates = {
            "A":{"state":"default"},
            "B":{"state":"default"},
            "C":{"state":"default"},
            "AB":{"state":"selected"},
            "AC":{"state":"default"},
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
            "C_BC":{"state":"crossed"}
        }
        result = check_answer(sectionStates, lineStates, False, invalid_syllogisms["cemostros"])
        self.assertEqual(self.is_correct(result), True)

    def test_check_answer_bamori_invalid_should_return_true(self):
        sectionStates = {
            "A":{"state":"selected"},
            "B":{"state":"default"},
            "C":{"state":"default"},
            "AB":{"state":"crossed"},
            "AC":{"state":"selected"},
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
        result = check_answer(sectionStates, lineStates, False, invalid_syllogisms["bamori"])
        self.assertEqual(self.is_correct(result), True)

    def test_check_answer_detise_invalid_should_return_true(self):
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
        result = check_answer(sectionStates, lineStates, False, invalid_syllogisms["detise"])
        self.assertEqual(self.is_correct(result), True)

    def test_check_answer_baroca_invalid_should_return_true(self):
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
        result = check_answer(sectionStates, lineStates, False, invalid_syllogisms["baroca"])
        self.assertEqual(self.is_correct(result), True)

    # Valid syllogisms completed incorrectly
    def test_check_answer_barbara_incorrect_diagram_valid_should_return_false(self):
        sectionStates = {
            "A":{"state":"selected"},
            "B":{"state":"default"},
            "C":{"state":"selected"},
            "AB":{"state":"default"},
            "AC":{"state":"crossed"}, #1 mistake
            "BC":{"state":"selected"},
            "ABC":{"state":"default"}
        }
        lineStates = {
            "AB_ABC":{"state":"default"},
            "AC_ABC":{"state":"default"},
            "BC_ABC":{"state":"crossed"}, #2 mistake
            "A_AB":{"state":"default"},
            "B_AB":{"state":"default"},
            "A_AC":{"state":"default"},
            "C_AC":{"state":"default"},
            "B_BC":{"state":"default"},
            "C_BC":{"state":"default"}
        }
        result = check_answer(sectionStates, lineStates, True, valid_syllogisms["barbara"])
        self.assertEqual(self.is_correct(result), False)
        self.assertEqual(result["main_answer_correct"], True)
        #check the two errors were detected correctly
        self.assertEqual(result["incorrect_sections"], {'AC': {'actual': 'crossed', 'expected': 'selected'}})
        self.assertEqual(result["incorrect_lines"], {'BC_ABC': {'actual': 'crossed', 'expected': 'default'}})

    def test_check_answer_ferio_incorrect_diagram_valid_should_return_false(self):
        sectionStates = {
            "A":{"state":"default"},
            "B":{"state":"default"},
            "C":{"state":"selected"}, #mistake
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
            "B_BC":{"state":"crossed"}, #mistake
            "C_BC":{"state":"default"}
        }
        result = check_answer(sectionStates, lineStates, True, valid_syllogisms["ferio"])
        self.assertEqual(self.is_correct(result), False)
        self.assertEqual(result["main_answer_correct"], True)
        #check the two errors were detected correctly
        self.assertEqual(result["incorrect_sections"], {'C': {'actual': 'selected', 'expected': 'default'}})
        self.assertEqual(result["incorrect_lines"], {'B_BC': {'actual': 'crossed', 'expected': 'default'}})

    def test_check_answer_datisi_incorrect_diagram_valid_should_return_true(self):
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
            "AC_ABC":{"state":"crossed"}, #mistake
            "BC_ABC":{"state":"default"},
            "A_AB":{"state":"default"},
            "B_AB":{"state":"default"},
            "A_AC":{"state":"crossed"}, #mistake
            "C_AC":{"state":"default"},
            "B_BC":{"state":"default"},
            "C_BC":{"state":"crossed"} #mistake
        }
        result = check_answer(sectionStates, lineStates, True, valid_syllogisms["datisi"])
        self.assertEqual(self.is_correct(result), False)
        self.assertEqual(result["main_answer_correct"], True)
        #check the 3 errors were detected correctly
        self.assertEqual(result["incorrect_sections"], {})
        self.assertEqual(result["incorrect_lines"], {'AC_ABC': {'actual': 'crossed', 'expected': 'default'}, 'A_AC': {'actual': 'crossed', 'expected': 'default'}, 'C_BC': {'actual': 'crossed', 'expected': 'default'}})

    def test_check_answer_baroco_incorrect_diagram_invalid_should_return_false(self):
        sectionStates = {
            "A":{"state":"default"},
            "B":{"state":"crossed"}, #mistake
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
            "B_AB":{"state":"crossed"}, #mistake
            "A_AC":{"state":"default"},
            "C_AC":{"state":"default"},
            "B_BC":{"state":"default"},
            "C_BC":{"state":"default"}
        }
        result = check_answer(sectionStates, lineStates, False, valid_syllogisms["baroco"])
        self.assertEqual(self.is_correct(result), False)
        self.assertEqual(result["main_answer_correct"], False)
        #check the two errors were detected correctly
        self.assertEqual(result["incorrect_sections"], {'B': {'actual': 'crossed', 'expected': 'selected'}})
        self.assertEqual(result["incorrect_lines"], {'B_AB': {'actual': 'crossed', 'expected': 'default'}})

    def test_check_answer_bocardo_incorrect_diagram_invalid_should_return_false(self):
        sectionStates = {
            "A":{"state":"selected"},
            "B":{"state":"default"},
            "C":{"state":"default"},
            "AB":{"state":"default"}, #mistake
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
        result = check_answer(sectionStates, lineStates, False, valid_syllogisms["bocardo"])
        self.assertEqual(self.is_correct(result), False)
        self.assertEqual(result["main_answer_correct"], False)
        #check the error was detected correctly
        self.assertEqual(result["incorrect_sections"], {'AB': {'actual': 'default', 'expected': 'selected'}})
        self.assertEqual(result["incorrect_lines"], {})

    def test_check_answer_dimaris_incorrect_diagram_invalid_should_return_false(self):
        sectionStates = {
            "A":{"state":"selected"},
            "B":{"state":"default"},
            "C":{"state":"default"},
            "AB":{"state":"selected"},
            "AC":{"state":"default"},
            "BC":{"state":"default"},
            "ABC":{"state":"default"} #mistake
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
        result = check_answer(sectionStates, lineStates, False, valid_syllogisms["dimaris"])
        self.assertEqual(self.is_correct(result), False)
        self.assertEqual(result["main_answer_correct"], False)
        #check the error was detected correctly
        self.assertEqual(result["incorrect_sections"], {'ABC': {'actual': 'default', 'expected': 'crossed'}})
        self.assertEqual(result["incorrect_lines"], {})

    # Invalid syllogisms completed incorrectly
    def test_check_answer_barbera_valid_should_return_false(self):
        sectionStates = {
            "A":{"state":"selected"},
            "B":{"state":"default"},
            "C":{"state":"default"},
            "AB":{"state":"default"},
            "AC":{"state":"selected"},
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
        result = check_answer(sectionStates, lineStates, True, invalid_syllogisms["barbera"])
        self.assertEqual(self.is_correct(result), False)

    def test_check_answer_barberi_valid_should_return_false(self):
        sectionStates = {
            "A":{"state":"selected"},
            "B":{"state":"default"},
            "C":{"state":"default"},
            "AB":{"state":"default"},
            "AC":{"state":"selected"},
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
        result = check_answer(sectionStates, lineStates, True, invalid_syllogisms["barberi"])
        self.assertEqual(self.is_correct(result), False)

    def test_check_answer_baroca_valid_should_return_false(self):
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
        result = check_answer(sectionStates, lineStates, True, invalid_syllogisms["baroca"])
        self.assertEqual(result["main_answer_correct"], False)
        self.assertEqual(self.is_correct(result), False)

    def test_check_answer_cemostros_incorrect_diagram_invalid_should_return_false(self):
        sectionStates = {
            "A":{"state":"default"},
            "B":{"state":"default"},
            "C":{"state":"default"},
            "AB":{"state":"selected"},
            "AC":{"state":"default"},
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
            "C_AC":{"state":"crossed"}, #mistake
            "B_BC":{"state":"default"},
            "C_BC":{"state":"crossed"}
        }
        result = check_answer(sectionStates, lineStates, False, invalid_syllogisms["cemostros"])
        self.assertEqual(self.is_correct(result), False)
        #check the error was detected correctly
        self.assertEqual(result["incorrect_lines"], {'C_AC': {'actual': 'crossed', 'expected': 'default'}})

    def test_check_answer_bamori_incorrect_diagram_invalid_should_return_false(self):
        sectionStates = {
            "A":{"state":"selected"},
            "B":{"state":"default"},
            "C":{"state":"default"},
            "AB":{"state":"crossed"},
            "AC":{"state":"selected"},
            "BC":{"state":"default"},
            "ABC":{"state":"selected"} #mistake
        }
        lineStates = {
            "AB_ABC":{"state":"default"},
            "AC_ABC":{"state":"default"},
            "BC_ABC":{"state":"default"},
            "A_AB":{"state":"default"},
            "B_AB":{"state":"default"},
            "A_AC":{"state":"crossed"}, #mistake
            "C_AC":{"state":"default"},
            "B_BC":{"state":"default"},
            "C_BC":{"state":"default"}
        }
        result = check_answer(sectionStates, lineStates, False, invalid_syllogisms["bamori"])
        self.assertEqual(self.is_correct(result), False)
        self.assertEqual(result["main_answer_correct"], True)
        #check the errors were detected correctly
        self.assertEqual(result["incorrect_sections"], {'ABC': {'actual': 'selected', 'expected': 'default'}})
        self.assertEqual(result["incorrect_lines"], {'A_AC': {'actual': 'crossed', 'expected': 'default'}})

    def test_check_answer_detise_incorrect_diagram_invalid_should_return_false(self):
        sectionStates = {
            "A":{"state":"crossed"}, #mistake
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
        result = check_answer(sectionStates, lineStates, False, invalid_syllogisms["detise"])
        self.assertEqual(result["main_answer_correct"], True)
        self.assertEqual(self.is_correct(result), False)
        #check the error was detected correctly
        self.assertEqual(result["incorrect_sections"], {'A': {'actual': 'crossed', 'expected': 'default'}})
        self.assertEqual(result["incorrect_lines"], {})


if __name__ == '__main__':
    unittest.main()
