class solution(object):
    def containsduplicate(self,nums):
        s=set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False        
nums = [1,2,3,1]
sol = solution()
result=sol.containsduplicate(nums)
print(result)