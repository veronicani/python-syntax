def any7(nums):
    """Are any of these numbers a 7? (True/False)"""

    # YOUR CODE HERE

    # if nums.count(7) > 0:
    #     return True
    # else:
    #     return False

    # return 'True' if nums.count(7) > 0 else 'False'
    return 'True' if nums.count(7) > 0 else 'False'

    # count(nums, 7)


print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))

# print("should be True", any7([1, 2, 7, 4, 5]))
# print("should be False", any7([1, 2, 4, 5]))
