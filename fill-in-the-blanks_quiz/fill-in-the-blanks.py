"""Fill-in-the-Blanks Quiz"""

""" This quiz will prompt a user with a paragraph containing several blanks.
The user should then be asked to fill in each blank appropriately to complete the paragraph.
This can be used as a study tool to help you remember important vocabulary!"""

instruction ='''This quiz will prompt you with a paragraph containing several blanks which you'll need to fill.
Each blank contains a little number and can appear multiple times, so read through the text carefully.
When you're ready, start typing in the blanks you're asked for. If you succeed, the whole text will be printed.
If you type text, the text will be displayed again. Answers will not be handled case-sensitive!'''
easy_quiz = '''In ___1___ theory, the normal (or ___2___) ___3___ is a very common ___4___ probability ___3___.'''
easy_replacement_vars = [['___1___', 'probability'], ['___2___', "Gaussian"], ['___3___', "distribution"], ['___4___', 'continuous']]
moderate_quiz = '''Cascading ___1___ Sheets (___2___) is a style sheet ___3___ used for describing the presentation of a ___4___ written in a markup ___3___.'''
moderate_replacement_vars = [['___1___', 'Style'], ['___2___', "CSS"], ['___3___', "language"], ['___4___', 'document']]
hard_quiz = '''In probability theory, the central ___1___ theorem (___2___) establishes that, for the most commonly studied scenarios, when ___3___ random variables are added, their sum tends toward a normal distribution (commonly known as a ___4___ curve) even if the original variables themselves are not ___5___ distributed.'''
hard_replacement_vars = [['___1___', 'limit'], ['___2___', 'CLT'], ['___3___', 'independent'], ['___4___', 'bell'], ['___5___', 'normally']]



def set_quiz():
    """set quiz text dependant on the difficulty variable"""
    if difficulty == 'easy':
        quiz = easy_quiz
        return quiz
    elif difficulty == 'moderate':
        quiz = moderate_quiz
        return quiz
    elif difficulty == 'hard':
        quiz = hard_quiz
        return quiz
    else:
        print 'Quiz not found'

def set_replacement_vars():
    """set quiz text replacement vars dependant on the difficulty variable"""
    if difficulty == 'easy':
        replacement_vars = easy_replacement_vars
        return replacement_vars
    elif difficulty == 'moderate':
        replacement_vars = moderate_replacement_vars
        return replacement_vars
    elif difficulty == 'hard':
        replacement_vars = hard_replacement_vars
        return replacement_vars
    else:
        print 'Quiz not found'

def input_game_difficulty():
    """Asking the user to choose between 'easy', 'moderate' or 'hard'
    Validating the response and returning the chosen difficulty"""
    difficulty = raw_input("Choose the difficulty! Enter 'easy', 'moderate' or 'hard' and hit enter: ")
    while difficulty not in ('easy', 'moderate', 'hard'):
        raw_input("Sorry, I did not unterstand that! Please choose between 'easy', 'moderate' and 'hard': ")
    return difficulty

def input_num_tries():
    """Asking the pick number of allowed tries
    see https://docs.python.org/2/tutorial/errors.html -> 8.3. Handling Exceptions"""
    while True:
        try:
            tries = int(raw_input("Tweak the difficulty! Choose the max number of tries: "))
            return tries
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

def get_solution(word, solution, replacement_vars):
    """Goes through the [placeholder, solution] list and checks for the correct pair."""
    tries = 0
    while True:
        user_solution = raw_input("Which word can be used to replace " + str(word) + " ?")
        if user_solution.lower() == solution.lower():
            print("Nice, you got it!")
            return
        else:
            tries += 1
            if tries == allowed_tries:
                print("You passed the number of allowed tries. You failed!")
                quit()
            print("Sorry, that was not correct. Try again!")

def replace_quiz(quiz, replacement_holders):
    """checks for placeholders, promts the user for solution and replaces them with those"""
    for replacement_holder in replacement_holders:
        blank = replacement_holder[0]
        solution = replacement_holder[1]
        get_solution(blank, solution, replacement_vars)
        quiz = quiz.replace(blank, solution)
        print quiz
    print("Awesome, you made it.")

def main():
    print instruction
    difficulty = input_game_difficulty()
    quiz = set_quiz()
    replacement_vars = set_replacement_vars()
    allowed_tries = input_num_tries()
    print quiz
    replace_quiz(quiz, replacement_vars)

main()
