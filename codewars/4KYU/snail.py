def snail(snail_map):
    n = len(snail_map)
    
    if n == 0 or snail_map == [[]]:  # edge case
        return []
    
    controller = []
    ans = []
    for b in range(n):
        temp = []
        for c in range(n):
            temp.append('s')
        controller.append(temp)
        
    controller[0][0] = 'a'
    
    _x = 0
    _y = 0
    pos_mov = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    ans.append(snail_map[0][0])

    
    
    while len(ans) < n**2:
        print(ans)
        for mov in pos_mov:
            contr = True
            while contr:
                if _x + mov[0] >= 0 and _y + mov[1] >= 0 and _x + mov[0] < n and _y + mov[1] < n:
                    if controller[_x + mov[0]][_y + mov[1]] == 's':
                        controller[_x + mov[0]][_y + mov[1]] = 'a'
                        ans.append(snail_map[_x + mov[0]][_y + mov[1]])
                        _x += mov[0]
                        _y += mov[1]
                    else:
                        contr = False
                else:
                    contr = False
    return ans
    