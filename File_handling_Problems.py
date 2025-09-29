# Swapping values in a List
List = [23, 12]
List[0], List[1] = List[1], List[0]

print(f"swapped list = {List}")

# Print second largest from list
List = [12, 4, 23, 45, 2, 56, 47]
Max = 0
secLarge = 0

for i in List:
    if i > Max:
        secLarge = Max
        Max = i
    else:
        secLarge = i

print(f"second largest from {List} is {secLarge}")

# Sorting a list without using sort()
randList = [1, 89, 2, 4, 76, 56, 6, 14, 23 ]
maximum = 0
poppedMax = []
orderedList = []

for i in randList:
    if i > maximum:
        orderedList.append(i)
        maximum = i
    else:
        poppedMax.append(orderedList.pop(-1))
        orderedList.append(i)
        maximum = i
orderedList.extend(poppedMax[:: -1])

print(f"Ordered List of {randList} is {orderedList}")

# < -----  Practice problems related exception handling and debugging  ---- >
# Problem 1:
def safeDivision(a, b):
    try:
        divide = a / b
        return divide
    except:
        return "Can't divide by zero!"

print(safeDivision(2, 0))
print(safeDivision(12, 6))

# Problem 2:
while True:
    try:
        num = int(input("Enter the valid integer: "))
        print("Thank You :)")
        break
    except ValueError:
        print("Invalid input! try again..!")

# Problem 3:
try:
    with open("data.txt", "r") as f:
        read = f.read()
        print(read)
except FileNotFoundError:
    print("File Not Found!")
    
finally:
    print("Operation complete!")

# Problem 4:
def chkPositive(num):
    if num > 0:
        return "Positive number."
    else:
        return "Number must be positive!"
    
print(chkPositive(-6))

# Problem 5:
try:
    text = input("Enter your text: ")
    with open("output.txt", "w") as File:
       File.write(text)

    with open("output.txt", "r") as File:
       reader = File.read()

    print(reader)
       
except IOError:
    print("Could not write to file!")
finally:
    print("Writing Complete :)")

# Problem 6:
try:
    with open("log.txt", "r") as f:
        r = f.read()
    with open("log.txt", "a") as f:
        append = f.write("Welcome in the world of Python!")
    print(r)

except FileNotFoundError:
    print("File not found, creating new file!")
    with open("log.txt", "w") as f:
        append = f.write("Welcome in the world of Python!")

    with open("log.txt", "r") as f:
        r = f.read()
    print(r)

finally:
    print("Operation done.")

# Problem 7:
def multiply_list(lst):
    print(f"list = {lst}")
    result = 0
    for num in lst:
        result *= num  # Bug is in this line as multiplying numbers with zero.
    print(f"num = {num}")
    return result

print(multiply_list([1, 2, 3, 4]))

# Problem 8:
try:
    num = int(input("Enter the number: "))
    divideNum = 100 / num
    print(f"100 / {num} = {divideNum}")
except ValueError:
    print("Not a number!")
except ZeroDivisionError:
    print("Can't divide to zero.")