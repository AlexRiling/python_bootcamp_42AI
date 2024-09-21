import sys

Nested_morse = {
    " ": "/",
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..",
    "J": ".---", "K": "-.-", "L": ".-..", "M": "--",
    "N": "-.", "O": "---", "P": ".--.", "Q": "--.-",
    "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----."
}

def sos(sentence):
    """
    Converts a given sentence into Morse code.
    Supports alphabetic characters (A-Z, a-z), numeric characters (0-9), and spaces.

    Parameters:
    sentence (str): The string to convert to Morse code.

    Returns:
    None: Prints the Morse code string with each character separated by a space.

    Raises:
    AssertionError: If the input contains any unsupported characters.
    """
    morse = []
    for letter in sentence:
        if letter.upper() in Nested_morse:
            morse.append(Nested_morse[letter.upper()])
        else:
            raise AssertionError("the arguments are bad")
    print(" ".join(morse))

def main():
    """
    Main function that validates input arguments and calls the sos function.

    Raises:
    AssertionError: If the number of arguments is not exactly 1 or if the input contains unsupported characters.
    """
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")

    sentence = sys.argv[1]
    sos(sentence)

if __name__ == "__main__":
    main()
