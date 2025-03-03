from syllogism import Syllogism
from answer import Answer


def check_answer(sectionState, lineState, valid, json_syllogism):
    syllogism = Syllogism(json_syllogism)

    #Takes the text of the syllogism and parses it into a Syllogism object,
    #which contains the terms, figure and mood of the syllogism
    syllogism.parse()

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

    answer.resolve_inconsistencies()

    #Check if the student's answer matches the correct answer
    incorrectSections = {}
    incorrectLines = {}
    for section, state in sectionState.items():
        if state.get('state') != answer.section_state[section].value:
            incorrectSections[section] = {"expected": answer.section_state[section].value, "actual": state.get('state')}
    for line, state in lineState.items():
        if state.get('state') != answer.line_state[line].value:
            incorrectLines[line] = {"expected": answer.line_state[line].value, "actual": state.get('state')}

    return {"main_answer_correct": syllogism.is_valid() == valid,
        "incorrectSections": incorrectSections,
        "incorrectLines": incorrectLines
    }
