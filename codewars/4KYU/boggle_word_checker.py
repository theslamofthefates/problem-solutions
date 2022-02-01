def find_word_rec(check_board, mn_board, word, _x, _y, temp, pos_words = [], cur_step = 1):
    
    if len(temp) == len(word):
        pos_words.append(temp)
        return
    
    pos_movements = [(1, 1), (1, 0), (0, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
    
    for movement in pos_movements:
        try:
            if check_board[_x + movement[0]][_y + movement[1]] == 'n' and mn_board[_x + movement[0]][_y + movement[1]] == word[cur_step] and _x + movement[0] >= 0 and _y + movement[1] >= 0:
                check_board[_x + movement[0]][_y + movement[1]] = 'y'
                find_word_rec(check_board, mn_board, word, _x + movement[0], _y + movement[1], temp + mn_board[_x + movement[0]][_y + movement[1]], pos_words, cur_step + 1)
        except:
            continue





def find_word(board, word):    
    pos_cord = []
    
    for i in range(len(board)):
        for b in range(len(board[0])):
            if board[i][b] == word[0]:
                pos_cord.append([i, b])
    
    for _cord in pos_cord:
        check_board = []
        for i in range(len(board)):
            temp = []
            for b in range(len(board[0])):
                temp.append('n')
            check_board.append(temp)

        
        pos_words = []
        check_board[_cord[0]][_cord[1]] = 'y'
        find_word_rec(check_board, board, word, _cord[0], _cord[1], word[0], pos_words, 1)
        print(pos_words)
        
        for c in pos_words:
            if c == word:
                return True
    
    return False
