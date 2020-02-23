def odd_or_even(x):
    if x%2==0:
        return("Even")
    elif x%2==1:
        return("Odd")
    else:
        return("Invalid Input")

#######################################

for i in range(0,20,1):
    print (i, "is", odd_or_even(i))
