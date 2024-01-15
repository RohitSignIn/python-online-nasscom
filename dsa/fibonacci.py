# Print Value only respect to index 
def fibonacci(num):
    if(num == 0 or num == 1):
        return num
    
    return fibonacci(num-1)+fibonacci(num-2)

print(fibonacci(6))

# Print Fibonacci Series
