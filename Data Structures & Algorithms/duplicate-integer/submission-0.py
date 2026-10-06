class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for int in nums:
            if int in seen:
                return True
            else:
                seen.add(int)
        return False