class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for index, value in enumerate(nums):
            dic[nums[index]] = dic.get(nums[index], 0) + 1
        return sorted(dic, key=lambda x: dic[x], reverse=True)[:k]