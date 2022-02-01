def solver(cur_node, length, used, cur_length = 1, counter = []):
    pos_mov = {'A':['B', 'E', 'D', 'H', 'F'],
           'B':['A', 'C', 'D', 'E', 'F', 'G', 'I'],
           'C':['B', 'F', 'E', 'D', 'H'],
           'D':['A', 'B', 'E', 'H', 'G', 'C', 'I'],
           'E':['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I'],
           'F':['C', 'I', 'E', 'B', 'H', 'G', 'A'],
           'G':['D', 'H', 'B', 'F', 'E'],
           'H':['G', 'I', 'E', 'D', 'A', 'F', 'C'],
           'I':['H', 'F', 'E', 'D', 'B'],
        }
    
    if 'B' in used:
        pos_mov['A'].append('C')
        pos_mov['C'].append('A')
    
    if 'D' in used:
        pos_mov['A'].append('G')
        pos_mov['G'].append('A')
        
    if 'F' in used:
        pos_mov['C'].append('I')
        pos_mov['I'].append('C')
        
    if 'H' in used:
        pos_mov['G'].append('I')
        pos_mov['I'].append('G')
    
    if 'E' in used:
        pos_mov['A'].append('I')
        pos_mov['I'].append('A')
        pos_mov['G'].append('C')
        pos_mov['C'].append('G')
        
        pos_mov['B'].append('H')
        pos_mov['H'].append('B')
        pos_mov['D'].append('F')
        pos_mov['F'].append('D')
    
    if cur_length == length:
        counter.append('0')
        return
    
    else:
        for next_node in pos_mov[cur_node]:
            if next_node not in used:
                solver(next_node, length, used + [next_node], cur_length + 1, counter)
                

def count_patterns_from(firstPoint, length):
    if length <= 0 or length > 9:
        return 0
    
    ans = []
    solver(firstPoint, length, [firstPoint], 1, ans)
    
    return len(ans)
