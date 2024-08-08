# https://leetcode.cn/problems/jump-game/description/

# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

def canJump(nums=[3, 2, 1, 0, 4]):
    def dfs(i):
        if not i: return True
        j = i + 1 - 1
        while (j := j - 1) >= 0:
            if nums[j] + j >= i: return dfs(j)
        return False
    return dfs(len(nums) - 1)


print(canJump())
