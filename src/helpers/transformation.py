import unidecode

def remove_accents(input_str):
    return unidecode.unidecode(input_str)