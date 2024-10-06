class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        '''
        s1 = hello jane
        s2 = hello my name is jane
        
        '''
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")
        if len(s1) == len(s2):
            if s1 == s2: 
                return True
            else:
                return False
            
        while (len(s1) > 0 and len(s2) > 0 and s1[-1] == s2[-1]):
            s1.pop()
            s2.pop()
        while (len(s1) > 0 and len(s2) > 0 and s1[0] == s2[0]):
            s1.pop(0)
            s2.pop(0)
            
        if len(s2) == 0 or len(s1) == 0:
            return True
        
        return False
    