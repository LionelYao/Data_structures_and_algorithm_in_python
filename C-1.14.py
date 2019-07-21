def distinct_product(nums):
    length = len(nums)
    found = 0
    for i in range(length):
        for j in range(i+1,length):
            if (nums[i] * nums[j]) % 2 == 1:
                if not found:
                    found = 1
                else:
                    return False
    if found:
        return True
    return False
list1 = [1,2,3]
list2 = [1,3,5]
list3 = [2,2]
print(distinct_product(list1))
print(distinct_product(list2))
print(distinct_product(list3))
