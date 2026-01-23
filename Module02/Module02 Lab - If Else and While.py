# Name: Nathan Thomas
# Module02 Lab - If Else and While

"""
    Write a Python app that will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll. Your app will:
        ask for and accept a student's last name.
        quit processing student records if the last name entered is 'ZZZ'.
        ask for and accept a student's first name.
        ask for and accept the student's GPA as a float.
        test if the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List.
        test if the student's GPA is 3.25 or greater and, if so, print a message saying that the studnet has made the Honor Roll.
    Test your app using at least five students.
    Your header comments need to contain
        Your name
        The file name for your app
        A brief description of what your app will do
"""

DEANS_LIST: float = 3.5
DEANS_LIST_MSG: str = "You made the dean's List"
HONOR_ROLL: float = 3.25
HONOR_ROLL_MSG: str = "You made the Honor Roll"
SENTINEL: str = 'ZZZ'

first_name: str = ''
gpa: float = 0.0
INPUT_PROMPT1: str = 'Enter the first name of the student: '
INPUT_PROMPT2: str = 'Enter the GPA of the student: '

while True:
    first_name = input(INPUT_PROMPT1)
    if first_name.upper() != SENTINEL:
        gpa = float(input(INPUT_PROMPT2))
        if gpa >= DEANS_LIST:
            print(DEANS_LIST_MSG)
        elif gpa >= HONOR_ROLL:
            print(HONOR_ROLL_MSG)
    else:
        break