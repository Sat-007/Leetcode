class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rss = sorted(score, reverse=True)
        d={}
        m=[]

        for i in range(len(rss)):
            if i == 0:
                d[rss[i]] = "Gold Medal"
            elif i == 1:
                d[rss[i]] = "Silver Medal"
            elif i == 2:
                d[rss[i]] = "Bronze Medal"
            else:
                d[rss[i]] = str(i+1)
        for i in score:
            m.append(d[i])
        return m