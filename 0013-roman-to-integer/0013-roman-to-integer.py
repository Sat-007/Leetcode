class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {"I":1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        tot = 0 
        prev = 0 
        
        for c in s:
            cur = roman_values[c]
            if cur > prev:
                tot += cur - 2 * prev
            else:
                tot += cur
            prev = cur
            
        return tot