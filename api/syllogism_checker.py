class Syllogism:
    def __init__(self, json_syllogism):
        self.major_term = json_syllogism["major_term"]
        self.minor_term = json_syllogism["minor_term"]
        self.middle_term = json_syllogism["middle_term"]
        self.premise1 = json_syllogism["premise1"]
        self.premise2 = json_syllogism["premise2"]
        self.conclusion = json_syllogism["conclusion"]
        self.premise1_form = ""
        self.premise2_form = ""
        self.conclusion_form = ""
        self.figure = -1

class Answer:
    def __init__(self):
        self.section_state = {
        "A": "DEFAULT",
        "B": "DEFAULT",
        "C": "DEFAULT",
        "AB": "DEFAULT",
        "AC": "DEFAULT",
        "BC": "DEFAULT",
        "ABC": "DEFAULT"
    }
        self.line_state = {
        "AB_ABC": "DEFAULT",
        "AC_ABC": "DEFAULT",
        "BC_ABC": "DEFAULT",
        "A_AB": "DEFAULT",
        "B_AB": "DEFAULT",
        "A_AC": "DEFAULT",
        "C_AC": "DEFAULT",
        "B_BC": "DEFAULT",
        "C_BC": "DEFAULT"
    }
        self.valid = None

def find_form(proposition):
    firstWord = proposition.split()[0]
    if firstWord == "All":
        return "A"
    if firstWord == "No":
        return "E"
    if firstWord == "Some":
        if "not" in proposition:
            return "O"
        else:
            return "I"
    else:
        raise ValueError("Invalid proposition")

def find_subject(proposition):
    return proposition.split()[1]

def find_figure(major_term, minor_term, middle_term, premise1, premise2):
    premise1_subject = find_subject(premise1)
    premise2_subject = find_subject(premise2)

    if premise1_subject == middle_term:
        if premise2_subject == minor_term:
            return 1
        elif premise2_subject == middle_term:
            return 3
        else:
            raise ValueError("Syllogism is not in standard form") #could try to re-arrange form
    elif premise1_subject == major_term:
        if premise2_subject == minor_term:
            return 2
        elif premise2_subject == middle_term:
            return 4
        else:
            raise ValueError("Syllogism is not in standard form")
    else:
        raise ValueError("Syllogism is not in standard form")

def parse_syllogism(syllogism):
    #Find form of each proposition
    syllogism.premise1_form = find_form(syllogism.premise1)
    syllogism.premise2_form = find_form(syllogism.premise2)
    syllogism.conclusion_form = find_form(syllogism.conclusion)

    print(f"Mood is {syllogism.premise1_form}{syllogism.premise2_form}{syllogism.conclusion_form}")
    #Find figure of syllogism
    syllogism.figure = find_figure(syllogism.major_term, syllogism.minor_term, syllogism.middle_term, syllogism.premise1, syllogism.premise2)

def concat_sections(*args):
    string = ""
    for arg in args:
        string += arg
    return ''.join(sorted(string))

def apply_change_to_section(change, region, answer): #TODO: change could be an enum
    if region in answer.section_state:
        answer.section_state[region] = change
    else:
        raise ValueError("Invalid region")

def apply_change_to_line(change, region, answer):
    if region in answer.line_state:
        answer.line_state[region] = change
    else:
        raise ValueError("Invalid region")

def apply_premise(premise_form, subject, predicate, other, answer):
    if premise_form == 'A':
        apply_change_to_section('SELECTED', subject, answer)
        apply_change_to_section('SELECTED', concat_sections(subject, other), answer)
        return
    elif premise_form == 'E':
        apply_change_to_section('SELECTED', concat_sections(subject, predicate), answer)
        apply_change_to_section('SELECTED', concat_sections(subject, predicate, other), answer)
        return
    elif premise_form == 'I':
        #apply_change_to_section('CROSSED', concat_lines(subject, predicate), answer)
        #SP_SPO
        #cross line INTERSECTING SUBJECT AND PREDICATE
        return
    elif premise_form == 'O':
        #cross line INTERSECTING SUBJECT AND OTHER
        #S_SO
        return

def check_answer(sectionState, lineState, json_syllogism):
    for section, state in sectionState.items():
        print(f"received sectionState: {section} {state}")
    for line, state in lineState.items():
        print(f"received lineState: {line} {state}")
    syllogism = Syllogism(json_syllogism)

    #Takes the text of the syllogism and parses it into a Syllogism object,
    #which contains the terms, figure and mood of the syllogism
    parse_syllogism(syllogism)

    #Initialise the states of our 'correct answer'
    answer = Answer()

    #Codify middle as A, major as B, minor as C, to match the sectionState keys
    MIDDLE = "A"
    MAJOR = "B"
    MINOR = "C"

    #Apply first premise
    if syllogism.figure == 1 or syllogism.figure == 3: #i.e. first premise has form MIDDLE x MAJOR
        apply_premise(syllogism.premise1_form, MIDDLE, MAJOR, MINOR, answer)
    elif syllogism.figure == 2 or syllogism.figure == 4: #i.e. first premise has form MAJOR x MIDDLE
        apply_premise(syllogism.premise1_form, MAJOR, MIDDLE, MINOR, answer)
    else:
        raise ValueError("Invalid figure")

    #Apply second premise
    if syllogism.figure == 1 or syllogism.figure == 2: #i.e. second premise has form MINOR x MIDDLE
        apply_premise(syllogism.premise2_form, MINOR, MIDDLE, MAJOR, answer)
    elif syllogism.figure == 3 or syllogism.figure == 4: #i.e. second premise has form MIDDLE x MINOR
        apply_premise(syllogism.premise2_form, MIDDLE, MINOR, MAJOR, answer)

    #Check if the student's answer matches the correct answer
    for section, state in sectionState.items():
        if state != answer.section_state[section]:
            return False
    for line, state in lineState.items():
        if state != answer.line_state[line]:
            return False
    return True
