from typing import List

class Solution:
    def fullJustify(self, words: List[str], max_len: int) -> List[str]:
        if not words or len(words) == 0:
            return []

        res = []
        i = 0
        width = 0 
        cur_line = []
        
        while i < len(words):
            
            cur_word = words[i]
            
            if width + len(cur_word) <= max_len:
                cur_line.append(cur_word)
                width += len(cur_word) + 1
                i += 1
                
            else:
                spaces = max_len - width + len(cur_line)
                added = 0 
                j = 0 
                while added < spaces:
                    if j >= len(cur_line) - 1:
                        j = 0 
                    cur_line[j] += " "
                    added += 1
                    j += 1
                res.append("".join(cur_line))
                
                cur_line = []
                width = 0 
                
        for word in range(len(cur_line) - 1):
            cur_line[word] += " "
        cur_line[-1] += " " * (max_len - width + 1)
        res.append("".join(cur_line))
        
        return res