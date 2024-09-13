import string 

def text_analyzer(text=""):
    """Counts the number of uppercase, lowercase, punctuation, and spaces in a given text."""
    if not text:
        text = input("What is the text to analyze?\n")
    upper_case = sum(1 for char in text if char.isupper())
    lower_case = sum(1 for char in text if char.islower())
    spaces = sum(1 for char in text if char.isspace())
    punctuation = sum(1 for char in text if char in string.punctuation)

    print(f"Upper-case: {upper_case}")
    print(f"Lower-case: {lower_case}")
    print(f"Spaces: {spaces}")
    print(f"Punctuation: {punctuation}")











