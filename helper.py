import re

def update_absent_letters(guess, guess_result, absent_letters):
  updated_list = absent_letters.copy()
  for i in range(len(guess_result)):
    if (guess_result[i] == 'absent'):
      if (guess[i] not in updated_list):
        updated_list.append(guess[i])
  return updated_list

def update_present_letters(guess, guess_result, present_letters):
  updated_list = present_letters.copy()
  for i in range(len(guess_result)):
    if (guess_result[i] == 'present'):
      if (guess[i] not in updated_list[i]):
        updated_list[i] += guess[i]
  return updated_list

# '|' is used as a separator for the word bank
def build_regex(guess, guess_result, absent_letters, present_letters):
  regex_parts = ['', '', '', '', '']
  for i in range(len(guess_result)):
    if (guess_result[i] == 'correct'):
      regex_parts[i] = guess[i]
    elif (len(absent_letters) != 0 or present_letters[i] != ''):
      regex_parts[i] = '[^' + ''.join(absent_letters) + present_letters[i] + '|]'
  return re.compile("".join(regex_parts))

def check_present_letters_in_guess(guess, present_letters):
  for letter in present_letters:
    if letter not in guess:
      return False
  return True

def filter_for_present_letters(possible_guess_list, present_letters):
  filtered_list = []
  present_letters = ''.join(present_letters)
  for guess in possible_guess_list:
    if check_present_letters_in_guess(guess, present_letters):
      filtered_list.append(guess)
  return filtered_list

def get_possible_guess(guess, guess_result, absent_letters, present_letters, word_bank_file_name):
  regex = build_regex(guess, guess_result, absent_letters, present_letters)
  with open(word_bank_file_name, 'r') as f:
    long_word_bank_string = f.read()
    unfiltered_guess_list = re.findall(regex, long_word_bank_string)
    return filter_for_present_letters(unfiltered_guess_list, present_letters)