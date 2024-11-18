def countValidSelections(nums) -> int:
    res = [0]
    idx = 0
    while idx < len(nums):
        def do():
            if nums[idx] != 0:
                return
            def move(idx, dirc):
                numscopy = nums.copy()
                while idx < len(numscopy) and idx >= 0:
                    def go():
                        if numscopy[idx] == 0:
                            return dirc
                        numscopy[idx] -= 1
                        return dirc * -1
                    dirc = go()
                    idx += dirc
                if sum(numscopy) == 0:
                    res[0] += 1 
                return
            move(idx,1)
            move(idx,-1)
        do()
        idx += 1
    return res[0]
countValidSelections([0,35,69,0,64,13,24,22,77,0,39,0,35,0,84,15,5,30,98,72,96,0,74,0,0,0,2,25,15,35,0,34,0,6,50,0,0,55,61,75,0,0,0,0,0,59,75,0,11,23,0,0,44,0,84,91,91,0,26,100,74,0,20,79,33,80,0,14,12,78,48,65,7,91,0,85,0,0,24,7,44,0,0,74,77,47,0,0,9,0,0,8,0,43,35,0,49,8,95,0])