from itertools import permutations
def permute(nums):
        l2=[]
        for i in range(len(nums)):
            l1=[]
            m=nums[i]
            rem=[]
            rem=nums[:i]+nums[i+1:]
            for p in permutations(rem):
                l1.append([m]+list(p))
            l2+=l1
        for i in range(len(l2)):
            if l2[i]==nums:
                a=len(nums)-1
                while(a!=-1):
                    nums.pop(a)
                    a-=1
                nums+=l2[i+1]
                return nums

print(permute([2,1,3]))