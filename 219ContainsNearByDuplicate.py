def containsNearbyDuplicate(nums, k: int):
        for i in range(len(nums)):
            j=k-i
            while(j>0):
                if nums[i]==nums[j] and i!=j:
                    return True
                else:
                    j-=1
        return False

print(containsNearbyDuplicate([1,2,3,1,2,3],2))