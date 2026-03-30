class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, value in enumerate(nums):
            subtract = target - value

            if subtract in seen:
                return [seen[subtract], index]
            seen[value] = index

         #for i in range(len(nums)):
            #for j in range(i+1, len(nums)):
                #sum = nums[i] + nums[j]
                #if sum == target:
                    #return [i,j]