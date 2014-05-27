edges = {(1, 'a') : 2,
         (2, 'a') : 2,
         (2, '1') : 3,
         (3, '1') : 3}
accepting = [3]
def fsmsim(string, current, edges, accepting):
    if string == "":
        return current in accepting
    else:
        letter = string[0]
        x = (current, letter)
        if(x in edges):
            return fsmsim(string[1:], edges[x], edges, accepting)
        else:
            return False
print(fsmsim("aaa111", 1, edges, accepting))
print (fsmsim("a1", 1, edges, accepting))
print (fsmsim("aaaaaaaaaaaaaaaaaaaaaaaaa1", 1, edges, accepting))
print (fsmsim("a", 1, edges, accepting) == False)
print (fsmsim("1", 1, edges, accepting) == False)

