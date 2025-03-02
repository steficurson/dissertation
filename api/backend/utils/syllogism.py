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

    #Finds the form of a proposition (A, E, I, or O) given its text
    def find_form(self, proposition):
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

    #Finds the subject of a proposition given its text
    def find_subject(self, proposition):
        return proposition.split()[1]

    #Finds the figure of a syllogism (1, 2, 3 or 4)
    def find_figure(self, major_term, minor_term, middle_term, premise1, premise2):
        premise1_subject = self.find_subject(premise1)
        premise2_subject = self.find_subject(premise2)

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

    def parse(self):
      self.premise1_form = self.find_form(self.premise1)
      self.premise2_form = self.find_form(self.premise2)
      self.conclusion_form = self.find_form(self.conclusion)

      print(f"Mood is {self.premise1_form}{self.premise2_form}{self.conclusion_form}") #for debug, remove later
      self.figure = self.find_figure(self.major_term, self.minor_term, self.middle_term, self.premise1, self.premise2)

