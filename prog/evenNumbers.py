start = 10
end = 40

print("Even numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    if num % 2 == 0:
        print(num)