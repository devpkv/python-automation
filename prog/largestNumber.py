nums = [11, 30, 12, 46, 23, 56, 78, 90, 10, 67]
largest = nums[0]

for num in nums:
    if num > largest:
        largest = num   

print("Largest number in the list is:", largest)

print("Using built-in function, largest number is:", max(nums))