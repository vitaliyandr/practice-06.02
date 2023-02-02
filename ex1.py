try:
    import random
    nums = [random.randint(-100, 100) for _ in range(10)]
    print(nums)
    sum_neg = 0
    for num in nums:
        if num < 0:
            sum_neg += num
    print('sum_neg =', sum_neg)
    sum_even = 0
    for num in nums:
        if num % 2 == 0:
            sum_even += num
    print('sum_even =', sum_even)
    sum_odd = 0
    for num in nums:
        if num % 2 != 0:
            sum_odd += num
    prod_3 = 1
    for i, num in enumerate(nums):
        if i % 3 == 0:
            prod_3 *= num

    print('prod_3 =', prod_3)
    prod_min_max = 1
    min_num = min(nums)
    max_num = max(nums)
    for num in nums:
        if num > min_num and num < max_num:
            prod_min_max *= num
    print('prod_min_max =', prod_min_max)
    sum_pos = 0
    first_found = False
    last_found = False
    for num in nums:
        if num > 0 and first_found == False:
            first_found = True
        elif first_found == True and num > 0:
            sum_pos += num
        elif first_found == True and num < 0:
            last_found = True
        if last_found == True and num > 0:
            break
    print('sum_pos =', sum_pos)
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')