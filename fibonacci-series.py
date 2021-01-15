# Program for Fibonacci sequence

a = 0 # first term
b = 1 #second term

print('Fibonacci series:')

# printing fibonacci series 
print(a,b,end=' ')
for i in range(0,40): # upto 40 
    num = a+b
    a=b
    b=num
    print(num,end=' ')



    
#   a   b   num
#   0   1   1
#   1   1   2   
#   1   2   3
#   2   3   5