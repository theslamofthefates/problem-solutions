# @karabacak
# 2/14/2022


def spiralize(size):
    spiral = []
    for b in range(size):
        if b == 0:
            ls = []
            for c in range(size):
                ls.append(1)
            spiral.append(ls)
        else:
            temp = []
            for c in range(size):
                temp.append(0)
            spiral.append(temp)
    
    lk = size - 1
    cur_x = 0
    cur_y = size - 1
    contr = 0
    
    while lk >= 0:
        print(lk)
        if contr % 4 == 0: #to bottom
            for b in range(lk):
                spiral[cur_x + b][cur_y] = 1
            cur_x += lk
                
        
        elif contr % 4 == 1: # to left
            for b in range(lk):
                spiral[cur_x][cur_y - b] = 1
            cur_y -= lk
            lk -= 2
            
        elif contr % 4 == 2: # to up
            for b in range(lk):
                spiral[cur_x - b][cur_y] = 1
            cur_x -= lk
        
        else: #to right
            if size % 2 == 0:
                for b in range(lk):
                    spiral[cur_x][cur_y + b] = 1
                cur_y += lk
                lk -= 2
            else:
                for b in range(lk+1):
                    spiral[cur_x][cur_y + b] = 1
                cur_y += lk
                lk -= 2
            
        contr += 1
    
    for b in spiral:
        print(b)
    return spiral