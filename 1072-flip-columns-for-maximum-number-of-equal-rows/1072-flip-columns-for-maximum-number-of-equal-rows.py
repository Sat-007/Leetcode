class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        pattern_count = defaultdict(int)
    
        for row in matrix:
           
            base_pattern = tuple(row)
            flip_pattern = tuple(1 - x for x in row)

           
            if base_pattern < flip_pattern:
                pattern_count[base_pattern] += 1
            else:
                pattern_count[flip_pattern] += 1

        return max(pattern_count.values())