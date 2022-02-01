def path_finder_solver(check_board, mn_board, ss_c = [], _x = 0, _y = 0):

    pos_movements = [(1, 0), (0, 1), (0, -1), (-1, 0)]

    if _x == len(mn_board) - 1 and _y == len(mn_board[0]) - 1:
        ss_c.append(1)
        return


    for movement in pos_movements:
        try:
            if mn_board[_x + movement[0]][_y + movement[1]] == '.' and check_board[_x + movement[0]][_y + movement[1]] == 'n' and _x + movement[0] >= 0 and _y + movement[1] >= 0:
                check_board[_x + movement[0]][_y + movement[1]] = 'y'
                path_finder_solver(check_board, mn_board, ss_c, _x + movement[0], _y + movement[1])
            else:
                continue
        except:
            continue
    
def path_finder(maze):
    check_board = []
    mn_board = []
    
    mn_board = maze.split("\n")
        
    for b in range(len(mn_board)):
        hk = []
        for k in range(len(mn_board[0])):
            hk.append("n")
        check_board.append(hk)
    
    
    check_board[0][0] = 'y'

    all_pos = []
    path_finder_solver(check_board, mn_board, all_pos)

    for b in all_pos:
        if b == 1:
            return True
    return False
