class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newHash = set()
        for i in nums:
            if i in newHash:
                return True
            else:
                newHash.add(i)
        return False