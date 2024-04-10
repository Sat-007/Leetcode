class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        result = [0] *len(deck)
        
        q = deque(range(0,len(deck)))
        
        for n in deck:
          
            i = q.popleft()
            result[i] = n 
            if q:
                q.append(q.popleft())
            
    
        return result
            