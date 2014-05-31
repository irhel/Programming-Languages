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
                            
def nfsmtrim(edges, accepting):
        new_edges = {}
        new_accepting = accepting
        transitions = []
        for edge in edges:
                t = edges[edge]
                g = []
                for x in t:
                        if nfsmaccepts(x, edges, accepting, []) != None:
                                g += [x]
                if len(g) > 0:
                        new_edges[edge] = g
                        transitions += g
        for x in new_accepting:
                if x != 1 and x not in transitions:
                        new_accepting.remove(x)
                
        return (new_edges, new_accepting)




edges4 = { (1,'a') : [1] ,
           (1,'b') : [2,5] ,
           (2,'b') : [3] ,
           (3,'b') : [4] ,
           (3,'c') : [2,1,4] } 
accepting4 = [ 2 ] 

print(nfsmtrim(edges4, accepting4))
