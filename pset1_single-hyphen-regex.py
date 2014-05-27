

import re

regexp = r"[a-z]+(?:-?[a-z]+)?"



test_case_input = """the wide-field infrared survey explorer is a nasa
infrared-wavelength space telescope in an earth-orbiting satellite which
performed an all-sky astronomical survey. be careful of -tricky tricky-
hyphens --- be precise."""

test_case_output = ['the', 'wide-field', 'infrared', 'survey', 'explorer',
'is', 'a', 'nasa', 'infrared-wavelength', 'space', 'telescope', 'in', 'an',
'earth-orbiting', 'satellite', 'which', 'performed', 'an', 'all-sky',
'astronomical', 'survey', 'be', 'careful', 'of', 'tricky', 'tricky',
'hyphens', 'be', 'precise']

if re.findall(regexp, test_case_input) == test_case_output:
  print("Test case passed.")
else:
  print("Test case failed:")
  print(re.findall(regexp, test_case_input)) 
