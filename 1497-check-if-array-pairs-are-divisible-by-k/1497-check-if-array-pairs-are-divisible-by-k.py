class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        """
        arr 
        length n 
        int k
        divide the array in n/2 pairs sum of each pair is divisible by k 
        
        1 2 3 4 5 6 7 8 9 10 
        k = 5
        (1,9) (2,8) (3,7) (4,6) (5,10)
        now we know that array should be even in length 
        
        the sum of the pairs % k == 0 
        how to put them in pairs such that it is divisible by k
        """
        
        rem_count = [0] * k
        
        for num in arr:
            rem = num % k 
            rem_count[rem] += 1
            
        if rem_count[0] % 2 != 0:
            return False
        
        for i in range(1, (k // 2) + 1):
            if i != k - i:
                if rem_count[i] != rem_count[k - i]:
                    return False    
        
        if k % 2 == 0 and rem_count[k // 2] % 2 != 0:
            return False
        
        return True
        
        