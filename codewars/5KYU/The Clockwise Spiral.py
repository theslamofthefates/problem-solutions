# @karabacak

def create_spiral(n):
    if type(n) != int:  # edge case
        return []
    if n == 0:  # edge case
        return []
    ans = []
    
    for b in range(n):
        temp = []
        for c in range(n):
            temp.append('s')
        ans.append(temp)
        
    ans[0][0] = 1
    
    _x = 0
    _y = 0
    pos_mov = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    cur_num = 2
    
    while cur_num <= n**2:
        for mov in pos_mov:
            contr = True
            while contr:
                if _x + mov[0] >= 0 and _y + mov[1] >= 0 and _x + mov[0] < n and _y + mov[1] < n:
                    if ans[_x + mov[0]][_y + mov[1]] == 's':
                        ans[_x + mov[0]][_y + mov[1]] = cur_num
                        cur_num += 1
                        _x += mov[0]
                        _y += mov[1]
                    else:
                        contr = False
                else:
                    contr = False
    
    return ans