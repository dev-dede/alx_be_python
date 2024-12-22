# This code is simpler and for practicee
# size = int(input("Enter the size of the pattern: "))
# i = size

# while size > 0:
#     print("*" * i)
#     size -=1

# The code below is complex but uses nested loops to reach the learning objective using while loop
size = int(input("Enter the size of the pattern: "))
i = 0

while i < size:
    j = 0
    while j < size:
        print("*", end="")
        j +=1
    i +=1
    print()
