import os


def int_input_verification():
    try:
        return int(input("> "))
    except ValueError:
        print("Enter a number between 0-9\n")
        os.system("PAUSE")
