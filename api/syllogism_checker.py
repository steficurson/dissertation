class Syllogism:
    def __init__(self, json_syllogism):
        self.major_term = json_syllogism["major_term"]
        self.minor_term = json_syllogism["minor_term"]
        self.middle_term = json_syllogism["middle_term"]
        self.premise1 = json_syllogism["premise1"]
        self.premise2 = json_syllogism["premise2"]
        self.conclusion = json_syllogism["conclusion"]
        self.mood = ""
        self.figure = -1

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
    premise1_form = find_form(syllogism.premise1)
    premise2_form = find_form(syllogism.premise2)
    conclusion_form = find_form(syllogism.conclusion)
    mood = premise1_form + premise2_form + conclusion_form

    #Find figure of syllogism
    figure = find_figure(syllogism.major_term, syllogism.minor_term, syllogism.middle_term, syllogism.premise1, syllogism.premise2)
    print(f"Figure: {figure} and mood: {mood}")
    syllogism.figure = figure
    syllogism.mood = mood

def check_answer(sectionState, lineState, json_syllogism):
    for section, state in sectionState.items():
        print(f"received sectionState: {section} {state}")
    for line, state in lineState.items():
        print(f"received lineState: {line} {state}")
    syllogism = Syllogism(json_syllogism)

    parse_syllogism(syllogism)

    return {"message": "Success"}
