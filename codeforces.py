def superset(nums: list, snums: list, k: int) -> list:
    if nums is None:
        return snums
    else:
        #snums.append([a0])
        for i in range(k, len(nums)):
            snums.append(nums[i])
            print(snums)
            superset(nums, snums, i+1)
            snums.pop(-1)

nums = [1,5,11,5]
snums = []
k = 0
snums = superset(nums,snums,k)
print(snums)
