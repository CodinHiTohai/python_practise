def minimumPairRemoval(nums):
    nums = nums[:]   # copy
    ops = 0

    def is_non_decreasing(arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                return False
        return True

    while not is_non_decreasing(nums):
        min_sum = float('inf')
        idx = 0

        # find leftmost adjacent pair with minimum sum
        for i in range(len(nums) - 1):
            s = nums[i] + nums[i+1]
            if s < min_sum:
                min_sum = s
                idx = i

        # merge the pair
        merged = nums[idx] + nums[idx+1]
        nums[idx] = merged
        nums.pop(idx + 1)

        ops += 1

    return ops
