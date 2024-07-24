# https://leetcode.cn/problems/merge-sorted-array/
import ctypes


def problem(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3) -> None:
    k, i, j = len(nums1) - 1, ctypes.c_int(m - 1), ctypes.c_int(n - 1)
    while k >= 0:
        if i.value >= 0 and j.value >= 0:
            mx, v = max([i, nums1[i.value]], [j, nums2[j.value]], key=lambda x: x[1])
        else:
            mx, v = [i, nums1[i.value]] if j.value < 0 else [j, nums2[j.value]]
        nums1[k] = v
        mx.value -= 1
        k -= 1
    print(nums1)


problem()
