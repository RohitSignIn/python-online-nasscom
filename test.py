# print("Hello World!")
# a = input("Enter Number: ")
# print("The entered number is:", a)

# Even Odd
# no = 8
# if(no % 2 == 0):
#     print("Even")
# else:
#     print("Odd")


# Print 1 to 10
          
# for val in range(10, 0, -1):
#     print(val)

# i = 1
# while(i<11):
#     print(i)
#     i+=1

# def sum(a, b):
#     return a+b


# print(sum(2, 5))


def fibonacci(num):
    if(num == 0 or num == 1):
        return num
    
    num = fibonacci(num-1)+fibonacci(num-2)
    print(num, "=>", end="")
    return num

fibonacci(6)

