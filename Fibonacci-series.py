n = int(input('Enter the number:')) # taking input and typecasting

n1 = 0 # first term
n2 = 1 # second term
count = 0 

if n <= 0:
    print('Please enter a positive number!!')
else:
    while count < n: # upto n numbers
        print(n1) # printing
        nth = n1 + n2 # increasing value
        n1 = n2
        n2 = nth
        count += 1