
def terminals(grammar):
    non_terminals = []
    terminals = []
    for rule in grammar:
        non_terminals += [rule[0]]
        terminals += rule[1]
    terminals = [x for x in terminals if x not in non_terminals]
    return terminals

def cfgempty(grammar, symbol, visited):
    if type(symbol) is str: symbol = [symbol]
    flag = True
    for x in symbol:
        if x not in terminals(grammar):
            flag = False
    if flag:
        return symbol
    for x in range(len(symbol)):
        for rule in grammar:
            if rule[0] == symbol[x] and rule[0] not in visited:
                res = cfgempty(grammar, symbol[0:x] + rule[1] + symbol[x + 1 :], visited + [rule[0]])
                if res != None:
                    return res
    return None


grammar1 = [
    ("S", ["(", "S", ")"]),
    ("S", [])
    ]

print(cfgempty(grammar1, "S", []))


grammar2 = [
    ("S", ["P", "a"]),
    ("S", ["Q", "b"]),
    ("S", ["Q", "c"]),
    ("Q", ["Q"]),
    ("Q", ["P"]),
    ("P", ["Q"])
    ]
print(cfgempty(grammar2, "S", []))

grammar3 = [
    ("S", ["N", "SN"]),
    ("SN", ["Dude"]),
    ("N", ["The"]),
    ]
print(cfgempty(grammar3, "S", []))


