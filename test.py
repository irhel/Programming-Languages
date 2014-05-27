import re
print(re.findall(r"[0-9]", "1 + 2 + 3 + 4"));
print(re.findall(r"[0-9][0-9]", "0025xx333"));
print (re.findall(r"[0-1]+", "3 = 11, 0 = 0, 2 = 10"));
print (re.findall(r"[0-9]+|[a-z]+", "95.6% pure meth"));
print (re.findall(r"-[0-9]+|[0-9]+","-2-3+12=7"));
reg = r'"(?:[^\\]|(?:\\.))*"'
s = " \" She said \"no\" \", \"the dog\", \"I said \" yes \" "
reg1 = r"[0-9]+(?:-?[0-9]+)+"
s1 = "phones like 2-123, 222, 12-123-14 shoudl match, but 12--won't"
print (re.findall(reg1, s1))
