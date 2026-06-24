import random

# Predefined word list
words = ["python", "coding", "laptop", "gaming", "school"]

# Randomly choose a word
chosen_word = random.choice(words)

# Create display list
display = ["_"] * len(chosen_word)

# Game variables
incorrect_guesses = 0
max_guesses = 6
guessed_letters = []

print("===== HANGMAN GAME =====")

while incorrect_guesses < max_guesses and "_" in display:

    print("\nWord:", " ".join(display))
    print("Guessed Letters:", guessed_letters)
    print(f"Remaining Attempts: {max_guesses - incorrect_guesses}")

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in chosen_word:
        print("Correct Guess!")

        for index in range(len(chosen_word)):
            if chosen_word[index] == guess:
                display[index] = guess

    else:
        incorrect_guesses += 1
        print("Wrong Guess!")

# Final Result
if "_" not in display:
    print("\nCongratulations! You Won!")
    print("The word was:", chosen_word)

else:
    print("\nGame Over!")
    print("The correct word was:", chosen_word)
