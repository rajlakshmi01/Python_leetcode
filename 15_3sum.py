def threeSum(nums):
        sum1=0
        l2=[]
        l3=[]
        ak=[]
        for i in range(len(nums)):
            ak=nums
            for j in range(len(nums)):
                if i!=j:
                    k=(sum1-nums[i]-nums[j])
                    l1=[]
                    ak=nums[i+1:j-1]+nums[j+1:]
                    if k in ak and nums.index(k)!=(i or j):
                        l1.append(nums[i])
                        l1.append(nums[j])
                        l1.append(k)
                        l3=sorted(l1)
                        if l3 not in l2:
                            l2.append(l3)
        return l2

print(threeSum([1,2,-2,1]))