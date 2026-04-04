class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortColors(nums[:mid])
        right = self.sortColors(nums[mid:])

        result = []
        i=0
        j=0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i = i + 1
            else:
                result.append(right[j])
                j = j + 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        nums[:] = result
        return nums
        