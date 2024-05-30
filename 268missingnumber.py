def missingNumber(nums):
        a=min(nums)
        b=max(nums)
        for i in range(a,b):
            if i in nums:
                nums.remove(i)
            else:
                return i
print(missingNumber([1,2,4]))