class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  
        l2=[]
        for i in range(len(nums)):
            for k in range(i+1,len(nums)):
                if nums[i] + nums[k] == target:
                    l2.append(i)
                    l2.append(k)
                    return l2
                    break
                else:
                    continue
