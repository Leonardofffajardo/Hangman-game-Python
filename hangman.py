import tkinter as tk
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")

        self.word = self.choose_word()
        self.guessed_letters = set()
        self.attempts = 6

        self.word_label = tk.Label(self.master, text=self.display_word(), font=("Arial", 18))
        self.word_label.pack()

        self.guess_entry = tk.Entry(self.master, font=("Arial", 14))
        self.guess_entry.pack()

        self.submit_button = tk.Button(self.master, text="Guess", command=self.make_guess)
        self.submit_button.pack()

        self.message_label = tk.Label(self.master, text="", font=("Arial", 14))
        self.message_label.pack()

    def choose_word(self):
        words = ['python', 'hangman', 'programming', 'computer', 'keyboard', 'mouse', 'monitor']
        return random.choice(words)

    def display_word(self):
        return ' '.join(char if char in self.guessed_letters else '_' for char in self.word)

    def make_guess(self):
        guess = self.guess_entry.get().lower()

        if len(guess) != 1 or not guess.isalpha():
            self.message_label.config(text="Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            self.message_label.config(text="You've already guessed that letter.")
            return

        self.guessed_letters.add(guess)

        if guess in self.word:
            self.message_label.config(text="Correct guess!")
            if set(self.word) <= self.guessed_letters:
                self.message_label.config(text=f"Congratulations! You've guessed the word: {self.word}")
                self.submit_button.config(state="disabled")
        else:
            self.message_label.config(text="Incorrect guess!")
            self.attempts -= 1
            self.message_label.config(text=f"Attempts left: {self.attempts}")
            if self.attempts == 0:
                self.message_label.config(text=f"Sorry, you've run out of attempts. The word was: {self.word}")
                self.submit_button.config(state="disabled")

        self.word_label.config(text=self.display_word())
        self.guess_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
