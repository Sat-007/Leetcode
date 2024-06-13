class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis=[nums[0]]
        for i in range(1,len(nums)):
            if nums[i]>lis[-1]:
                lis.append(nums[i])
            elif nums[i]<=lis[-1]:
                low = 0
                high = len(lis) - 1
                while low < high:
                    mid = low + (high - low) // 2
                    if lis[mid] < nums[i]:
                        low = mid + 1
                    else:
                        high = mid

                lis[low]=nums[i]



        return len(lis)
                
        
        