def terminals(grammar):
    non_terminals = []
    terminals = []
    for rule in grammar:
        non_terminals += [rule[0]]
        terminals += rule[1]
    terminals = [x for x in terminals if x not in non_terminals]
    return terminals

def expand(current, grammar, visited):
    flag = True
    for symbol in current:
        if symbol not in terminals(grammar):
            flag = False
    if flag:
        yield current
    for pos in range(len(current)):
        for rule in grammar:
            if rule[0] == current[pos] and rule[0] not in visited:
                yield from expand(current[0:pos] + rule[1] + current[pos + 1 :], grammar, visited + [rule[0]])

def isambig(grammar, start, utterence):
    result = [i for i in expand([start], grammar, [])]
    result.sort()
    for x in range(len(result) - 1):
        if result[x] == result[x+1] and result[x] == utterence:
            return True
    return False
                
