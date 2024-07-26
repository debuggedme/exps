# https://leetcode.cn/problems/sort-an-array/description/

# 示例 1：

# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
# 示例 2：

# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]

def sortArray(nums=[5, 2, 3, 1]):
    def insertSort(nums):
        i = 0
        while i < len(nums):
            minidx = min([idx for idx in range(i, len(nums))], key=lambda x: nums[x])
            nums[minidx], nums[i] = nums[i], nums[minidx]
            i += 1
    insertSort(nums)
    return nums


sortArray()
