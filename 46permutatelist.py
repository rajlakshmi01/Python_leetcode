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
        return l2

print(permute([1,2,3]))