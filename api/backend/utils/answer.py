from utils.state_enums import SectionState, LineState
from utils.helpers import concat_sort

class Answer:
    adjacent_lines = {
        "A": ["A_AB", "A_AC"],
        "B": ["B_AB", "B_BC"],
        "C": ["C_AC", "C_BC"],
        "AB": ["A_AB", "B_AB", "AB_ABC"],
        "AC": ["A_AC", "C_AC", "AC_ABC"],
        "BC": ["B_BC", "C_BC", "BC_ABC"],
        "ABC": ["AB_ABC", "AC_ABC", "BC_ABC"]
    }

    def __init__(self):
        self.section_state = {
        "A": SectionState.DEFAULT,
        "B": SectionState.DEFAULT,
        "C": SectionState.DEFAULT,
        "AB": SectionState.DEFAULT,
        "AC": SectionState.DEFAULT,
        "BC": SectionState.DEFAULT,
        "ABC": SectionState.DEFAULT
        }
        self.line_state = {
        "AB_ABC": LineState.DEFAULT,
        "AC_ABC": LineState.DEFAULT,
        "BC_ABC": LineState.DEFAULT,
        "A_AB": LineState.DEFAULT,
        "B_AB": LineState.DEFAULT,
        "A_AC": LineState.DEFAULT,
        "C_AC": LineState.DEFAULT,
        "B_BC": LineState.DEFAULT,
        "C_BC": LineState.DEFAULT
        }
        self.selected_answer = None

    def apply_change_to_section(self, change, section):
        if section in self.section_state:
            self.section_state[section] = change
        else:
            raise ValueError("Invalid section", section)

    def apply_change_to_line(self, change, line):
        if line in self.line_state:
            self.line_state[line] = change
        else:
            raise ValueError("Invalid line", line)

    def apply_premise(self, premise_form, subject, predicate, other):
        if premise_form == 'A':
            self.apply_change_to_section(SectionState.SELECTED, subject)
            self.apply_change_to_section(SectionState.SELECTED, concat_sort(subject, other))
        elif premise_form == 'E':
            self.apply_change_to_section(SectionState.SELECTED, concat_sort(subject, predicate))
            self.apply_change_to_section(SectionState.SELECTED, concat_sort(subject, predicate, other))
        elif premise_form == 'I':
            self.apply_change_to_line(LineState.CROSSED, concat_sort(subject, predicate) + "_" + concat_sort(subject, predicate, other))
        elif premise_form == 'O':
            self.apply_change_to_line(LineState.CROSSED, subject + "_" + concat_sort(subject, other))
        else:
            raise ValueError("Invalid premise form", premise_form)

    def move_cross(self, line, empty_section):
        line_sections = line.split("_")
        non_empty_section = line_sections[0] if empty_section == line_sections[1] else line_sections[1]
        self.apply_change_to_line(LineState.DEFAULT, line)
        self.apply_change_to_section(SectionState.CROSSED, non_empty_section)

    #If a section is empty but borders a crossed line, move the cross to the other section
    def resolve_inconsistencies(self):
        for section, sectionState in self.section_state.items():
            if sectionState == SectionState.SELECTED:
                for line in self.adjacent_lines[section]:
                    if self.line_state[line] == LineState.CROSSED:
                        self.move_cross(line, section)
