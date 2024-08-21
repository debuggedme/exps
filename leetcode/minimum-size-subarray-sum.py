def minSubArrayLen(target=4, nums=[1, 4, 4]):
        res = None
        slow, fast = 0, 0
        while fast < len(nums):

            while slow <= fast and sum(nums[slow:fast + 1]) >= target:
                slow += 1
            if sum(nums[slow - 1:fast + 1]) >= target:
                res = min(fast + 1 - slow + 1, res if res else fast + 1 - slow + 1)

            fast += 1
        return res if res else 0


minSubArrayLen()
