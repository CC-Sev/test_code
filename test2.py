def my_decorator(func):
    def wrapper(test_case, nums):
        print(f'Running Test Case {test_case}')
        func(nums)
    return wrapper

@my_decorator
def my_function(nums):
    print(nums)

nums1 = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]
nums3 = [1, 0, 1, 0]
nums4 = [1, 1, 0, 1]
nums5 = [0, 1]

my_function(1, nums1)
my_function(2, nums2)
my_function(3, nums3)
my_function(4, nums4)
my_function(5, nums5)
