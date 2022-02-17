def longest_slide_down(pyramid):
    if len(pyramid) == 1:
        return pyramid[0]
    
    indx = len(pyramid) - 2
    ma = 0
    while indx >= 0:
        lsst = []
        for b in range(len(pyramid[indx])):
            lsst.append(max(pyramid[indx][b] + pyramid[indx + 1][b], pyramid[indx][b] + pyramid[indx + 1][b + 1]))
            pyramid[indx][b] = lsst[b]
        ma = max(lsst)
        indx -= 1
    
    return ma