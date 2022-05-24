import unittest

from regex_producer import build_each_avoid_regex, build_regex, filter_for_present_letters

class TestFormAbsentRegex(unittest.TestCase):
  def test_empty_absent_present(self):
    actual = build_each_avoid_regex(0, [], ['','','','',''])
    expected = ""
    self.assertEqual(actual, expected)

  def test_form_absent_regex_1(self):
    actual = build_each_avoid_regex(1, ['a','b','c'], ['d','e','','',''])
    expected = "[^abce]"
    self.assertEqual(actual, expected)

  # Note: present_letters and absent_letters are mutually exclusive.
  def test_form_absent_regex_2(self):
    actual = build_each_avoid_regex(3, ['l','u','t','e'], ['','','','',''])
    expected = "[^lute]"
    self.assertEqual(actual, expected)

  def test_form_absent_regex_3(self):
    actual = build_each_avoid_regex(3, ['l','u','t','e'], ['','o','r','a',''])
    expected = "[^lutea]"
    self.assertEqual(actual, expected)

class TestBuildRegex(unittest.TestCase):
  def test_absent_update(self):
    answer = 'favor'
    guess = 'flute'
    guess_result = ['correct', 'absent', 'absent', 'absent', 'absent']
    absent_letters = []
    present_letters = ['','','','','']
    build_regex(guess, guess_result, absent_letters, present_letters)
    actual = absent_letters
    expected = ['l','u','t','e']
    self.assertEqual(actual, expected)

  def test_present_update(self):
    answer = 'favor'
    guess = 'foray'
    guess_result = ['correct', 'absent', 'absent', 'absent', 'absent']
    absent_letters = []
    present_letters = ['','','','','']
    build_regex(guess, guess_result, absent_letters, present_letters)
    actual = present_letters
    expected = ['','o','r','a','']
    self.assertEqual(actual, expected)

  def test_basic_1(self):
    answer = 'favor'
    guess = 'flute'
    guess_result = ['correct', 'absent', 'absent', 'absent', 'absent']
    absent_letters = []
    present_letters = ['','','','','']
    actual = build_regex(guess, guess_result, absent_letters, present_letters)
    expected = ['f', '[^lute]', '[^lute]', '[^lute]', '[^lute]']
    self.assertEqual(actual, expected)

  def test_basic_2(self):
    answer = 'favor'
    prev_guess = 'flute'
    guess = 'foray'
    guess_result = ['correct', 'present', 'present', 'present', 'absent']
    absent_letters = ['l','u','t','e']
    present_letters = ['','','','','']
    actual = build_regex(guess, guess_result, absent_letters, present_letters)
    expected = ['f', '[^luteyo]', '[^luteyr]', '[^luteya]', '[^lutey]']
    self.assertEqual(actual, expected)

  def test_duplicates_in_specific_avoid(self):
    answer = 'catch'
    prev_guess = 'avoid'
    guess = 'abbbb'
    guess_result = ['present', 'absent', 'absent', 'absent', 'absent']
    absent_letters = 'voidb'
    present_letters = ['a', '', '', '', '']
    actual = build_regex(guess, guess_result, absent_letters, present_letters)[2]
    expected = ['a', '', '', '', ''] # we shouldn't get 'aa'
    self.assertEqual(actual, expected)

  def test_duplicate_in_absent_letters(self):
    answer = 'catch'
    prev_guess = 'avoid'
    guess = 'avoid'
    guess_result = ['present', 'absent', 'absent', 'absent', 'absent']
    absent_letters = ['v','o','i','d']
    present_letters = ['a', '', '', '', '']
    build_regex(guess, guess_result, absent_letters, present_letters)
    expected = ['v','o','i','d'] # nothing new should be added
    self.assertEqual(present_letters, expected)

class TestFilter(unittest.TestCase):
  def test_basic_1(self):
    possible_guess_list = ['favor', 'fable']
    specific_avoids = ['', 'o', 'r', 'a', '']
    actual = filter_for_present_letters(possible_guess_list, specific_avoids)
    expected = ['favor']
    self.assertEqual(actual, expected)

  def test_basic_2(self):
    possible_guess_list = ['venue', 'ven']
    specific_avoids = ['e', 'v', 'e', 'e', 'n']
    actual = filter_for_present_letters(possible_guess_list, specific_avoids)
    expected = ['venue', 'ven']
    self.assertEqual(actual, expected)