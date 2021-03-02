### Hangman game:-

import random

WORDS = 'words.txt'

class Hangman:
    def __init__(self):
        self.word = self.chooseWord(self.loadWords()).lower()
        self.main()
    def loadWords(self):
        print("Loading words from file..")
        file = open(WORDS, 'r')
        line = file.readline()
        wordList = line.split()
        print(f" {len(wordList)} words loaded")
        return wordList
    
    def chooseWord(self, wordList: list):
        return random.choice(wordList)
    
    def isWordGuessed(self, word: str, lettersGuessed: list):
        for letter in word:
            if letter in lettersGuessed:
                continue
            else:
                return False
        return True
    
    def getGuessedWord(self, word: str, lettersGuessed: list):
        def indices(letter: str, word: str):
            return [i for i in range(len(word)) if letter == word[i]]
        
        word = list(word)
        guessedWord = ['*'] * len(word)
        
        for letter in lettersGuessed:
            if letter in word:
                for xIndex in indices(letter, word):
                    guessedWord[xIndex] = letter
        return ''.join(guessedWord)
    
    def getAvailableLetters(self, lettersGuessed):
        notGuessed = []
        for i in range(97, 123):
            if chr(i) not in lettersGuessed:
                notGuessed.append(chr(i))
        return ''.join(notGuessed)
    
    def main(self):
        word = self.word
        lettersGuessed = []
        guessedWord = ''
        guesses = []
        count = 8
        print(f"I am thinking of a word that is {len(word)} letters long")
        while not self.isWordGuessed(word, lettersGuessed) and count != 0:
            availableLetters = self.getAvailableLetters(lettersGuessed)
            print(f"Available letters: {availableLetters}")
            guess = input(f"You have {count} lives left: ")
            while guess in lettersGuessed or guess in guesses:
                print("Guessed before! Pick another letter:", availableLetters)
                guess = input("Guess another letter: ")
            if guess in word:
                print("Correct!")
                guesses.append(guess)
                lettersGuessed.append(guess)
                guessedWord = self.getGuessedWord(word, lettersGuessed)
                print("Good guess! The word is:", guessedWord)
                if guessedWord == word:
                    print("You got the word, you win!")
                    break
                continue
            else:
                guesses.append(guess)
                print("Oops! That letter is not in my word:", self.getGuessedWord(word, lettersGuessed))
            count -= 1
        if count == 0:
            print("Sorry you ran out of guesses... \n but the word was,", word)

Hangman()


## AFTER NOTE:- This could easily have been written without classes. In this, the only advantage of a class design for the game is order and neatness. Other than that, I can't think of anythin else.