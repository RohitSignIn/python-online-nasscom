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

num = 5

for i in range(1, 11):
    print(num, "*", i, "=", num*i)