from syllogism import Syllogism
from answer import Answer
from state_enums import SectionState, LineState

def check_answer(sectionState, lineState, json_syllogism):
    for section, state in sectionState.items():
        print(f"received sectionState: {section} {state}")
    for line, state in lineState.items():
        print(f"received lineState: {line} {state}")
    syllogism = Syllogism(json_syllogism)

    #Takes the text of the syllogism and parses it into a Syllogism object,
    #which contains the terms, figure and mood of the syllogism
    Syllogism.parse()

    #Initialise the states of our 'correct answer'
    answer = Answer()

    #Codify middle as A, major as B, minor as C, to match the sectionState keys
    MIDDLE = "A"
    MAJOR = "B"
    MINOR = "C"

    #Apply first premise
    if syllogism.figure == 1 or syllogism.figure == 3: #i.e. first premise has form MIDDLE x MAJOR
        answer.apply_premise(syllogism.premise1_form, MIDDLE, MAJOR, MINOR)
    elif syllogism.figure == 2 or syllogism.figure == 4: #i.e. first premise has form MAJOR x MIDDLE
        answer.apply_premise(syllogism.premise1_form, MAJOR, MIDDLE, MINOR)
    else:
        raise ValueError("Invalid figure")

    #Apply second premise
    if syllogism.figure == 1 or syllogism.figure == 2: #i.e. second premise has form MINOR x MIDDLE
        answer.apply_premise(syllogism.premise2_form, MINOR, MIDDLE, MAJOR)
    elif syllogism.figure == 3 or syllogism.figure == 4: #i.e. second premise has form MIDDLE x MINOR
        answer.apply_premise(syllogism.premise2_form, MIDDLE, MINOR, MAJOR)

    # need more logic here to iron out contradictions, i.e. moving crosses

    #Check if the student's answer matches the correct answer
    #TODO: needs more nuance, give hollistic answer
    for section, state in sectionState.items():
        if state.get('state') != answer.section_state[section]:
            return False
    for line, state in lineState.items():
        if state.get('state') != answer.line_state[line]:
            return False
    return True
