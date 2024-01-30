# a = [2,2,3,4,1,4,-12,-2,0]

# countPos = 0
# countNeg = 0
# countZeros = 0

# for i in a:
#     if(i > 0):
#         countPos += 1
#     elif(i < 0):
#         countNeg += 1
#     else:
#         countZeros += 1


# print("+ve Count: ", countPos)
# print("-ve Count: ", countNeg)
# print("Zeros Count: ", countZeros)



# Maximum number
# a = []

# for i in range(5):
#     data = int(input("Enter a number: "))
#     a.append(data)

# max = a[0]

# for i in a:
#     if(max < i):
#         max = i

# print("Max: ", max)


# 3. First Even No

# for i in range(11):
#     if(i == 5):
#         break
#     print(i)

# 3. First Even No || First Odd No

# nums = [1,3,3,5,6,8,9]

# gotEven = False
# for i in nums:
#     if(i % 2 == 0):
#         gotEven = True
#     if(gotEven):
#         print(i)


# 7. Display sum of all two digits and three digits Number

# num = 237
# # Typecasting - "237"
# num = str(num)

# sum = 0

# for i in num:
#     sum += int(i)

# print(sum)



# 4. Maximum Second Number - Approach 1
# nums = [1,2,5,8,5,6,9]

# max = 0
# secondMax = 0

# if(nums[0] > nums[1]):
#     max = nums[0]
#     secondMax = nums[1]
# else:
#     max = nums[1]
#     secondMax = nums[0]

# for i in nums:
#     if(max < i):
#         secondMax = max
#         max = i
#     elif(secondMax < i):
#         secondMax = i

# print("secondMax is:", secondMax)
# print("Max is:", max)


# 10. Table
# num = 5

# for i in range(1, 11):
#     print(num, "*", i, "=", num*i)


# 9. Display second Even without skipping the rest Odd

# list1 = [2,3,4,5,6,2,4,5]

# evenCount = 0

# for i in list1:
#     if(i % 2 == 0):
#         evenCount += 1
#     else:
#         print(i)

#     if(evenCount == 2):
#         print(i)
#         evenCount += 1


# def name(name, greetings):
#     print(greetings, "My name is", name)
    

# name("Mohit", "Hello")




# LIST - Mutable
# a = [1,"hello",4,5,True,7,8]
# a[0] = 8
# print(type(a))

# # Tuple - Immutable
# b = (1,"hello",4,5,True,7,8)
# print(type(b))


# Dictionary
# a = [0,0,"Hello",1,1,2,"Hello",2]

# dict = {}
# for i in a:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1

# print(dict)

# Sets
# thisset = ({"apple", "banana", "cherry"})

# print(thisset)


# Anonympous Function
sum = lambda a, b: a + b


print(sum(2, 3))










