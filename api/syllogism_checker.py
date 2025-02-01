
def find_form(proposition):
    firstWord = proposition.split()[0]
    if firstWord == "All":
        return "A"
    if firstWord == "No":
        return "E"
    if firstWord == "Some":
        if proposition.contains("not"):
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
    major_term = syllogism["major_term"] #aka predicate
    minor_term = syllogism["minor_term"] #aka subject
    middle_term = syllogism["middle_term"]

    premise1 = syllogism["premise1"]
    premise2 = syllogism["premise2"]
    conclusion = syllogism["conclusion"]

    #Find form of each proposition
    premise1_form = find_form(premise1)
    premise2_form = find_form(premise2)
    conclusion_form = find_form(conclusion)

    mood = premise1_form + premise2_form + conclusion_form

    #Find figure of syllogism
    figure = find_figure(major_term, minor_term, middle_term, premise1, premise2)
    print(f"Figure: {figure}")
    print(f"Mood: {mood}")

    return figure, mood

def check_answer(sectionState, lineState, syllogism):
    for section, state in sectionState.items():
        print(f"received sectionState: {section} {state}")
    for line, state in lineState.items():
        print(f"received lineState: {line} {state}")
    print(f"received syllogism: {syllogism}")

    figure, mood = parse_syllogism(syllogism)

    return {"message": "Success"}
