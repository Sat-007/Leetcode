class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ''
        for char in s:
            if char == ' ':
                if word:
                    words.append(word)
                    word = ''
            else:
                word += char
       
        if word:
            words.append(word)

        
        reversed_words = []
        for i in range(len(words)-1, -1, -1):
            reversed_words.append(words[i])

       
        reversed_s = ''
        for i in range(len(reversed_words)):
            reversed_s += reversed_words[i]
            if i < len(reversed_words) - 1:
                reversed_s += ' '
                
        return reversed_s