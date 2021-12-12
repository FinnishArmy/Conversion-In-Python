'''Miles To Kilometers'''

def milesToKilo(miles):
#My Conversion Factor
     return miles*1.60934

def milesToKiloTest():
#Converts 1 Mile to Kilomters
    print('Testing 1 Mile')
    if milesToKilo(1) == 1.60934:
        print('Correct')
    else:
        print('Wrong!!')
#Converts 10 Mile to Kilomters
    print('Testing 10 Miles')
    if milesToKilo(10) == 16.0934:
        print('Correct')
    else: print('Wrong!!')
#Converts 20 Mile to Kilomters
    print('Testing 20 Miles')
    if milesToKilo(20) == 32.1868:
        print('Correct!')
    else: print('Wrong!')
#Converts 40 Mile to Kilomters
    print('Testing 40 Miles')
    if milesToKilo(40) == 64.3736:
        print('Correct!')
    else: print('Wrong!')

milesToKiloTest()




'''BuiltIn Function'''

def builtin(x):
#Calculate x to the power of 3
    print('Calculating ' + str(x)  + ' to the power of 3. This equals: ' + str(pow(x,3)))

#Convert x to an integer by truncating
    print('Truncating ' + str(x) + ' to: ' + str(int(x)))

#Convert x to an integer rounding
    print('Rounding ' + str(x) + ' to: ' + str(round(x)))

#Take the absolute value of x and convert it to a float
    print('Taking the absolute value of: ' + str(x) + ' = ' + str(abs(x)) + ' Converting to float: ' + str(float(x)))

builtin(2)
