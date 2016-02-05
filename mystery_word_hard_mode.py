
import random
with open("/usr/share/dict/words") as word_file:
    secret_words = word_file.read().splitlines()

print("Welcome to Secret Word! \n")
def difficulty_level_input():
    word_length = None
    while word_length is None:
        try:
            difficulty_level = int(input("\nChoose your difficulty level from 1 to 3:> "))

            if difficulty_level == 1:
                word_length = random.randrange(4, 6)
                return word_length
            elif difficulty_level == 2:
                word_length = random.randrange(6, 10)
                return word_length
            elif difficulty_level == 3:
                word_length = random.randrange(10, 26)
                return word_length
            else:
                print("Please enter only 1, 2 or 3")
                continue
        except ValueError:
            print("Please enter only 1, 2 or 3")

def game():

    word_length = difficulty_level_input()
    secret_word = random.choice([x for x in secret_words if len(x) == word_length])
    bad_guesses = 8
    already_guessed = []
    word_display = list("_" * len(secret_word))
    print("\nGuess one letter per round. Guesses are not case sensitive.\n"
          "Can you get it right with only {} bad guesses? \n"
          "This word has {} letters.\n".format(bad_guesses, len(secret_word)))

    print(word_display)
    print("\nBad Guesses Left: {}".format(bad_guesses))

    while word_display != list(secret_word):

        guess = input("Guess a letter> ").lower()

        if len(guess) > 1:
            print("Please enter one letter at a time.")
            pass
        elif not guess.isalpha():
            print("Please enter only letters!")
            pass
        else:
            if guess not in already_guessed:
                counter = 0
                for letter in secret_word:
                    if letter == guess:
                        word_display[counter] = guess
                    counter += 1
                if guess not in secret_word:
                    print("Sorry. Bad Guess.\n")
                    bad_guesses -= 1
                if bad_guesses < 0:
                    print("Sorry, Better Luck Next Time.\n"
                          "The Secret Word Was: {}".format(secret_word))
                    break
                already_guessed.append(guess)

            else:
                print("You Already Guessed That Letter! Try Again.")

        print(word_display)
        print("\nBad Guesses Left: {}".format(bad_guesses))
        print("\nAlready Guessed Letters:", already_guessed)

    if input("Good Game! Want To Play Again? Y/n: ").lower() == 'y':
        game()
game()
