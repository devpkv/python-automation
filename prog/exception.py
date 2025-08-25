try: 
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result is:", result)
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")
except Exception as e:
    print("An unexpected error occurred:", str(e))      
finally:
    print("Execution completed.")