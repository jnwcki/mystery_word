
import random
with open("/usr/share/dict/words") as word_file:
    secret_words = word_file.read().splitlines()
secret_word = random.choice([x for x in secret_words if len(x) > 3])
bad_guesses = 8
already_guessed = []
word_display = list("_" * len(secret_word))
print("Welcome to Secret Word! \n"
      "Guess one letter per round. Guesses are not case sensitive.\n"
      "Can you get it right with only {} bad guesses? \n"
      "This word has {} letters.\n".format(bad_guesses, len(secret_word)))

print(word_display)
print("\nBad Guesses Left: {}".format(bad_guesses))
while word_display != list(secret_word):
    guess = input("Guess a letter> ").lower()
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