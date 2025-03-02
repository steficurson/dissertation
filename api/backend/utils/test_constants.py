valid_syllogisms = {
    "barbara": { #AAA-1
        "premise1":"All M are P",
        "premise2":"All S are M",
        "conclusion":"All S are P",
        "major_term":"P",
        "middle_term":"M",
        "minor_term":"S",
        "question_id":1,
        "tutorial_id":1,
        "valid":True
    },
    "celarent": { #EAE-1
        "premise1":"No M are P",
        "premise2":"All S are M",
        "conclusion":"No S are P",
        "major_term":"P",
        "middle_term":"M",
        "minor_term":"S",
        "question_id":1,
        "tutorial_id":1,
        "valid":True
    },
    "camestres": {  #AEE-2
        "premise1":"All P are M",
        "premise2":"No S are M",
        "conclusion":"No S are P",
        "major_term":"P",
        "middle_term":"M",
        "minor_term":"S",
        "question_id":1,
        "tutorial_id":1,
        "valid":True
    },
    "darii": { #AII-1
        "premise1":"All M are P",
        "premise2":"Some S are M",
        "conclusion":"Some S are P",
        "major_term":"P",
        "middle_term":"M",
        "minor_term":"S",
        "question_id":1,
        "tutorial_id":1,
        "valid":True
    },
    "disamis": { #IAI-3
        "premise1":"Some M are P",
        "premise2":"All M are S",
        "conclusion":"Some S are P",
        "major_term":"P",
        "middle_term":"M",
        "minor_term":"S",
        "question_id":1,
        "tutorial_id":1,
        "valid":True
    },
    "ferio": { #EIO-1
        "premise1":"No M are P",
        "premise2":"Some S are M",
        "conclusion":"Some S are not P",
        "major_term":"P",
        "middle_term":"M",
        "minor_term":"S",
        "question_id":1,
        "tutorial_id":1,
        "valid":True
    },
    "baroco": { #AOO-2
        "premise1":"All P are M",
        "premise2":"Some S are not M",
        "conclusion":"Some S are not P",
        "major_term":"P",
        "middle_term":"M",
        "minor_term":"S",
        "question_id":1,
        "tutorial_id":1,
        "valid":True
    },
    "bocardo": { #OAO-3
        "premise1":"Some M are not P",
        "premise2":"All M are S",
        "conclusion":"Some S are not P",
        "major_term":"P",
        "middle_term":"M",
        "minor_term":"S",
        "question_id":1,
        "tutorial_id":1,
        "valid":True
    },
}

invalid_syllogisms = {
  "barbera": { #AEA-1
      "premise1":"All M are P",
      "premise2":"No S are M",
      "conclusion":"All S are P",
      "major_term":"P",
      "middle_term":"M",
      "minor_term":"S",
      "question_id":1,
      "tutorial_id":1,
      "valid":False
  },
  "barberi": { #AEI-1
      "premise1":"All M are P",
      "premise2":"No S are M",
      "conclusion":"Some S are P",
      "major_term":"P",
      "middle_term":"M",
      "minor_term":"S",
      "question_id":1,
      "tutorial_id":1,
      "valid":False
  },
  "cemostros" : { #EOO-2
      "premise1":"No P are M",
      "premise2":"Some S are not M",
      "conclusion":"Some S are not P",
      "major_term":"P",
      "middle_term":"M",
      "minor_term":"S",
      "question_id":1,
      "tutorial_id":1,
      "valid":False
  },
  "bamori" : { #AOI-3
      "premise1":"All M are P",
      "premise2":"Some M are not S",
      "conclusion":"Some S are P",
      "major_term":"P",
      "middle_term":"M",
      "minor_term":"S",
      "question_id":1,
      "tutorial_id":1,
      "valid":False
  },
}
