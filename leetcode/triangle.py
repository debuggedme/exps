# https://leetcode.cn/problems/triangle/

# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# 输出：11
# 解释：如下面简图所示：
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

import functools


def problem(triangle=[[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]):
    @functools.cache
    def dfs(i, j):
        if not (i < len(triangle) and j < len(triangle[i])):
            return 0
        return triangle[i][j] + min(dfs(i + 1, j), dfs(i + 1, j + 1))
    return dfs(0, 0)


print(problem())
