# Find squares of numbers
import time 
start_time = time.time() #start time of the program
nums = [i for i in range(1, 1000000)]# list comprehension to generate a list of numbers from 1 to 1000000
squares = []
for n in nums:
    squares.append(n ** 2)# append the square of the number to the list
print(len(squares))
print(time.time() - start_time)
end_time = time.time()