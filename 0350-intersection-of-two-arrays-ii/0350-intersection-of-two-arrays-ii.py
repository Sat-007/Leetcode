class Solution:
  def intersect(self, num1: List[int], num2: List[int]) -> List[int]:
    num1.sort()
    num2.sort()
    i = j = 0 
    res = []
    
    while i < len(num1) and j < len(num2):
        if num1[i] < num2[j]:
            i += 1
        elif num1[i] > num2[j]:
            j += 1
        else:
            res.append(num1[i])
            i += 1
            j += 1
    return res