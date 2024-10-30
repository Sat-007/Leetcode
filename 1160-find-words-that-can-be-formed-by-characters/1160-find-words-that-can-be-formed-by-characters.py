class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0 
        count = collections.Counter(chars)
        res = []

        for word in words:
            if set(word) - set(chars):
                continue
            words_count = Counter(word)
            good = True
            for c,freq in words_count.items():
                #print(count[c])
                if count[c] < freq:
                    good = False
                    break
            if good:
                ans += len(word)
                res.append(word)
        print(res)
        return ans
                    