nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nums_2 = [x for x in nums if x % 2 == 0]
print(nums_2)

nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nums_3 = [x for x in nums if x % 2 != 0]
print(nums_3)

nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nums_4 = [x for x in nums if x < 0]
print(nums_4)

nums = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
nums_5 = [x for x in nums if x > 0]
print(nums_5)
