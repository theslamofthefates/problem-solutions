def get_pin_solver(_x, _y):
    num_pad = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        ['k', 0, 'k']
    ]
    pos = []
    pos.append(num_pad[_x][_y])
    pos_mov = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    
    for mov in pos_mov:
        
        try:
            if type(num_pad[_x + mov[0]][_y + mov[1]]) == int and _x + mov[0] >= 0 and _y + mov[1] >= 0:
                pos.append(num_pad[_x + mov[0]][_y + mov[1]]) 
        except:
            continue
    return pos
 

def nested_depth(lst, depth, cur_depth = 0, temp = "", mn_lst = []):
    if cur_depth == depth:
        mn_lst.append(temp)
        return
    
    else:
        for b in range(len(lst[cur_depth])):
            nested_depth(lst, depth, cur_depth + 1, temp + str(lst[cur_depth][b]), mn_lst)
    
    


def get_pins(observed):

    num_pad_coord = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
        0: [3, 1],
    }
    
    ans = []
    
    
    for b in observed:
        b = int(b)
        ans.append(get_pin_solver(num_pad_coord[b][0], num_pad_coord[b][1]))
    
    ss_ans = []
    nested_depth(ans, len(ans), 0, "", ss_ans)        
    return ss_ans
