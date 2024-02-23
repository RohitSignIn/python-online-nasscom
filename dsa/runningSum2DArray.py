def runningSum(nums):
    i = 1
    while(i<len(nums)):
        nums[i] = nums[i] + nums[i-1]
        i+=1

    return nums

print(runningSum([1,2,3,4]))