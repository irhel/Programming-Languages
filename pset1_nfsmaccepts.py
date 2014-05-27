
edges = { (1, 'a') : [2, 3],
          (2, 'a') : [2],
          (3, 'b') : [4, 2],
          (4, 'c') : [5] }
accepting = [5] 

edges2 = { (1, 'a') : [1],
           (2, 'a') : [2] }
accepting2 = [2]

def nfsmaccepts(current, edges, accepting, visited):
        if current in accepting:
                return ""
        if current in visited:
                return None
        else:
                possible_transitions = []
                for edge in edges:
                        if edge[0] == current:
                                for p in edges[edge]:
                                        res = nfsmaccepts(p, edges, accepting, visited + [current])
                                        if res != None:
                                                return edge[1] + res
                                        
print("Test 1: " + str(nfsmaccepts(1, edges, accepting, []) == "abc"))
print("Test 2: " + str(nfsmaccepts(1, edges, [4], []) == "ab"))
print("Test 3: " + str(nfsmaccepts(1, edges2, accepting2, []) == None))
print("Test 4: " + str(nfsmaccepts(1, edges2, [1], []) == ""))
