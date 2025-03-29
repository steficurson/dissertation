#helper function which concatenates strings and sorts them alphabetically
#used to generate the correct state key for a given (inter)section or line relationship
def concat_sort(*args):
    string = ""
    for arg in args:
        string += arg
    return ''.join(sorted(string))
