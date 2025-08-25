str = "malayalam"
is_palindrome = True

for i in range(len(str) // 2):
    
    print(i, len(str) - 1 - i, str[i], str[len(str) - 1 - i])

    if str[i] != str[len(str) - 1 - i]:
        is_palindrome = False
        break

if is_palindrome:
    print(str, "is a palindrome")

else:
    print(str, "is not a palindrome")