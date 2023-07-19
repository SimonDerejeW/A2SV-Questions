class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        lis = list(range(0,len(nums)+1))
       
        for i in sorted(lis):
            if i in nums:
                lis.remove(i)
        for i in lis:
            return i
