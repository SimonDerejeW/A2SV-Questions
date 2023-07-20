class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_list = sorted(nums)
        lis = []
        for i in range(len(sorted_list)):
            if sorted_list[i]==target:
                lis.append(i)
        return lis
