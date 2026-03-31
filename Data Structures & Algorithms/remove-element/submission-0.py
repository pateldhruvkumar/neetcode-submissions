class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for index, value in enumerate(nums):
            if value != val:      
                nums[k] = value
                k += 1
        return k