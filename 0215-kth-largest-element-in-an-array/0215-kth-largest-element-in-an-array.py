class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = nums[:k]
        heapq.heapify(min_heap)  # O(k)

        # Process the remaining elements in the array
        for num in nums[k:]:
            if num > min_heap[0]:
                heapq.heapreplace(min_heap, num)  # O(log k)

        return min_heap[0] 