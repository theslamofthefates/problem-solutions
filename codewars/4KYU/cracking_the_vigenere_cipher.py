def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def get_key_length(cipher_text, max_key_length):
    gcds = {}
    for pos_key in range(2, max_key_length):
        freqs = {}
        for b in range(0, len(cipher_text), pos_key):
            if cipher_text[b: b + pos_key] not in freqs:
                freqs[cipher_text[b: b + pos_key]] = [b]
            else:
                freqs[cipher_text[b: b + pos_key]].append(b)
        diffs = []
        for b in freqs:
            if len(freqs[b]) > 1:
                for c in range(1, len(freqs[b])):
                    for ss in range(c):
                        diffs.append(freqs[b][c] - freqs[b][ss])

        for first in range(1, len(diffs)):
            for second in range(first):
                if gcd(diffs[first], diffs[second]) in gcds:
                    gcds[gcd(diffs[first], diffs[second])] += 1
                else:
                    gcds[gcd(diffs[first], diffs[second])] = 1

    ls = sorted(gcds.items(), key = lambda x: x[1], reverse=True)    
    if ls[0][0] == 2:
        return ls[1][0]//2
    elif max_key_length > ls[0][0]:
        return ls[0][0]
    return ls[0][0]//2
    