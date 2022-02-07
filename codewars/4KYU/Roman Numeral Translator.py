# @karabacak
class RomanNumerals:

    def to_roman(val):
        gnu = {1000: 'M', 900: 'CM', 500:'D', 400: 'CD', 100:'C', 90: 'XC', 50:'L', 40:'XL', 10 :'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        ans = ""
        for b in gnu:
            ans += val//b * gnu[b]
            val -= val//b * b
            
        return ans

    def from_roman(roman_num):
        gnu = {'I':1, 'IV':4, 'V':5, 'IX': 9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}
        
        indx = 0
        ans = 0
        while indx < len(roman_num):
            try:
                if roman_num[indx] + roman_num[indx + 1] in gnu:
                    ans += gnu[roman_num[indx] + roman_num[indx + 1]]
                    indx += 2
                    continue
                else:
                    ans += gnu[roman_num[indx]] 
                    indx += 1
                    continue
            except:
                ans += gnu[roman_num[indx]] 
                indx += 1
                continue
        return ans