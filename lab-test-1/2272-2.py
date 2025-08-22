def sum_even_odd(numbers):
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        if num % 2 == 0:
            even_sum += num
        else:
            odd_sum += num
    return even_sum, odd_sum

# Take input from user
nums = input("Enter numbers separated by spaces: ")
nums_list = [int(x) for x in nums.split()]

even, odd = sum_even_odd(nums_list)
print("Sum of even:", even)
print("Sum of odd:", odd)