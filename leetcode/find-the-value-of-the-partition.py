
# 示例 1：

# 输入：nums = [1,3,2,4]
# 输出：1
# 解释：可以将数组 nums 分成 nums1 = [1,2] 和 nums2 = [3,4] 。
# - 数组 nums1 的最大值等于 2 。
# - 数组 nums2 的最小值等于 3 。
# 分区值等于 |2 - 3| = 1 。
# 可以证明 1 是所有分区方案的最小值。
# 示例 2：

# 输入：nums = [100,1,10]
# 输出：9
# 解释：可以将数组 nums 分成 nums1 = [10] 和 nums2 = [100,1] 。
# - 数组 nums1 的最大值等于 10 。
# - 数组 nums2 的最小值等于 1 。
# 分区值等于 |10 - 1| = 9 。
# 可以证明 9 是所有分区方案的最小值。

def findValueOfPartition(nums=[]):
    return min([abs(t[i] - t[i + 1]) for i in range(len(nums) - 1)]) if (t := sorted(nums)) else 0


print(findValueOfPartition())
