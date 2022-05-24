from re import A
from unicodedata import name
from helper import get_possible_guess, update_absent_letters, update_present_letters

def main():
  absent_letters = []
  present_letters = ['','','','','']
  
  while True:
    guess = input("Enter guess: \n")
    guess_result = []

    for i in range(5):
      guess_result.append(input(f"Enter guess result for index {i + 1}:"))

    absent_letters = update_absent_letters(guess, guess_result, absent_letters)
    present_letters = update_present_letters(guess, guess_result, present_letters)
    print(get_possible_guess(guess, guess_result, absent_letters, present_letters, 'large.txt'))


if __name__ == "__main__":
  main()