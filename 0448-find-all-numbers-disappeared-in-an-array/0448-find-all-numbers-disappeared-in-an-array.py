class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            num = abs(nums[i])
            if nums[num - 1] > 0:
                nums[num - 1] = -nums[num - 1]

        # Collect all indices where the value is positive (meaning the number is missing)
        missing_numbers = []
        for i in range(len(nums)):
            if nums[i] > 0:
                missing_numbers.append(i + 1)

        return missing_numbers