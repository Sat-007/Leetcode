class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        l = 0 
        r = len(s) - 1
        
        
        '''
        I c e C r e a A m
        0 1 2 3 4 5 6 7 8           
        l               r
      
        '''
        while l < r:
            if s[l] not in vowels:
                l += 1
                
            elif s[r] not in vowels:
                r -= 1
            else:
                s[l],s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)
            
            
            