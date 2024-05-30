def containsDuplicate(nums):
        if len(nums)==2:
            if nums[0]==nums[1]:
                return True 
        for i in range(len(nums)):
            a=nums[:i]+nums[i+1:]
            if nums[i] in a:
                return True
        return False

print(containsDuplicate([1,5,-2,-4,0]))