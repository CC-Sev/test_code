nums = [1,2,3,4,5,6,7,8,9,10]

def while_swap_nums(num_list):
    left = 0
    right = len(num_list) - 1    
    while left < right:
        num_list[left], num_list[right] = num_list[right], num_list[left]
        left += 1
        right -= 1
print("WHILE LOOP:")
print(nums)
while_swap_nums(nums)
print(nums)

def for_swap_nums(num_list):
    for i in range(len(num_list) // 2):
        num_list[i], num_list[-i-1] = num_list[-i-1], num_list[i]
print("\nFOR LOOP:")
print(nums)
for_swap_nums(nums)
print(nums)