from utils.syllogism import Syllogism
from utils.answer import Answer


def check_answer(section_state, line_state, selected_answer, json_syllogism):
    syllogism = Syllogism(json_syllogism)

    #Takes the text of the syllogism and parses it into a Syllogism object,
    #which contains the terms, figure and mood of the syllogism
    syllogism.parse()

    #Initialise the states of our 'correct answer'
    answer = Answer()

    #Codify middle as A, major as B, minor as C, to match the section_state keys
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
    incorrect_sections = {}
    incorrect_lines = {}
    for section, state in section_state.items():
        if state.get('state') != answer.section_state[section].value:
            incorrect_sections[section] = {"expected": answer.section_state[section].value, "actual": state.get('state')}
    for line, state in line_state.items():
        if state.get('state') != answer.line_state[line].value:
            incorrect_lines[line] = {"expected": answer.line_state[line].value, "actual": state.get('state')}

    #Suggest a hollistic mark
    nr_incorrect_sections_and_lines = len(incorrect_sections) + len(incorrect_lines)
    main_answer_correct = syllogism.is_valid() == selected_answer
    suggested_mark = -1
    if main_answer_correct:
        if nr_incorrect_sections_and_lines > 10:
            suggested_mark = 0
        else:
            suggested_mark = 10 - nr_incorrect_sections_and_lines
    else:
        if nr_incorrect_sections_and_lines > 7:
            suggested_mark = 0
        else:
            suggested_mark = 7 - nr_incorrect_sections_and_lines


    return {"main_answer_correct": main_answer_correct,
        "incorrect_sections": incorrect_sections,
        "incorrect_lines": incorrect_lines,
        "suggested_mark": suggested_mark,
        "selected_answer": selected_answer
    }
