def encode_rail_fence_cipher(string, n):
    general_list = []
    for b in range(n):
        general_list.append([])
    ss = 0
    for c in range(len(string)//(2 * n - 2) + 1):
        try:
            for b in range(2 * n - 2):
                if b < n:
                    general_list[b].append(string[ss + b])

                else:
                    general_list[2 * n - 2 - b].append(string[ss + b])
            ss+= 2 * n - 2
        except:
            continue
    
    res = ""
    for b in general_list:
        for k in b:
            res += k
    return res
    
def decode_rail_fence_cipher(string, n):
    general_list = []
    for b in range(n):
        general_list.append([])
    ss = 0
    for c in range(len(string)//(2 * n - 2) + 1):
        try:
            for b in range(2 * n - 2):
                if b < n:
                    general_list[b].append(string[ss + b])
                else:
                    general_list[2 * n - 2 - b].append(string[ss + b])
            ss+= 2 * n - 2
        except:
            continue
    
    gn = []
    for b in range(n):
        gn.append([])
        
    
    b = 0    
    for l in range(n):
        gn[l] = string[b:b + len(general_list[l])]
        b += len(general_list[l])
    
    res = ""
    
    tour_1 = 0
    tour_2 = 0

    for c in range(len(string)//(2 * n - 2) + 1):
        try:
            for k in range(2 * n - 2):
                if k < n and (k == 0 or k == n - 1):
                    res += gn[k][tour_1]        
                elif k < n and (k != 0 and k != n - 1):
                    res += gn[k][tour_2]        
                else:
                    res += gn[2 * n - 2 - k][tour_2 + 1]
            tour_1 += 1
            tour_2 += 2
        except:
            continue
        
    return res
