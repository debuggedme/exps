# https://leetcode.cn/problems/remove-element

def removeElement(nums=[], val=2):
    i, j = 0, len(nums) - 1
    while i < j:
        while i < j and nums[j] == val:
            j -= 1
        while i < j and nums[i] != val:
            i += 1
        if i != j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    return j if j >= 0 and nums[j] == val else j + 1


print(removeElement())
