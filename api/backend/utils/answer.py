from state_enums import SectionState, LineState

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
        "A": "default",
        "B": "default",
        "C": "default",
        "AB": "default",
        "AC": "default",
        "BC": "default",
        "ABC": "default"
    }
        self.line_state = {
        "AB_ABC": "default",
        "AC_ABC": "default",
        "BC_ABC": "default",
        "A_AB": "default",
        "B_AB": "default",
        "A_AC": "default",
        "C_AC": "default",
        "B_BC": "default",
        "C_BC": "default"
    }
        self.valid = None

    def concat_sort(self, *args):
        string = ""
        for arg in args:
            string += arg
        return ''.join(sorted(string))

    def apply_change_to_section(self, change, region):
        if region in self.section_state:
            self.section_state[region] = change
        else:
            raise ValueError("Invalid region", region)

    def apply_change_to_line(self, change, line):
        if line in self.line_state:
            self.line_state[line] = change
        else:
            raise ValueError("Invalid line", line)

    def apply_premise(self, premise_form, subject, predicate, other):
        if premise_form == 'A':
            self.apply_change_to_section(SectionState.SELECTED, subject)
            self.apply_change_to_section(SectionState.SELECTED, self.concat_sort(subject, other))
        elif premise_form == 'E':
            self.apply_change_to_section(SectionState.SELECTED, self.concat_sort(subject, predicate))
            self.apply_change_to_section(SectionState.SELECTED, self.concat_sort(subject, predicate, other))
        elif premise_form == 'I':
            self.apply_change_to_line(SectionState.CROSSED, self.concat_sort(subject, predicate) + "_" + self.concat_sort(subject, predicate, other))
        elif premise_form == 'O':
            self.apply_change_to_line(SectionState.CROSSED, subject + "_" + self.concat_sort(subject, predicate))
        else:
            raise ValueError("Invalid premise form", premise_form)

    def move_cross(self, line, empty_section): #TODO
        return

    #If a section is empty but borders a crossed line, move the cross to the other section
    def resolve_inconsistencies(self):
        for section, state in self.section_state.items():
            if state == SectionState.SELECTED:
                for line, state in self.adjacent_lines[section]:
                    if state == LineState.CROSSED:
                        self.move_cross(line, section)
