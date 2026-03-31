class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}

        for index, value in enumerate(nums):
            dic[nums[index]] = dic.get(nums[index], 0) + 1
        return max(dic, key=lambda k: dic[k])