import re

def sumnums(sentence):
    l = re.findall(r"[0-9]+", sentence);
    if(l == []): return 0;
    res = 0
    for e in l:
        res+=(int)(e)
    return res         

test_case_input = """The Act of Independence of Lithuania was signed 
on February 16, 1918, by 20 council members."""

test_case_output = 1954

if sumnums(test_case_input) == test_case_output:
  print("Test case passed.")
else:
  print("Test case failed:")
  print(sumnums(test_case_input)) 
