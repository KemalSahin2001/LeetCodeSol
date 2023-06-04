def longestConsecutive(self ,nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if(len(nums) == 0): return 0
    nums = list(set(nums))
    nums.sort()
    max_count = 0
    count = 0

    for i in range(len(nums) - 1):
        if((nums[i] + 1) == nums[i+1]):
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    if(max_count == 0): return 1
    else: return max_count + 1