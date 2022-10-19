# just adding a comment to push the code!

def convert_100_to_celsius():

#     # Convert a temperature of 100 degrees fahrenheit to celsius
#     # Save this to a variable called celsius_100, and use print() to print out the value
#     # Is the resulting temperature you get an integer or float?
#     # Print 'float' if it is a float or 'int' if it is an int
#     # How do you know? Write a comment below your code explaining how you know which it is
    f = 100
    celcius_100 = ( f - 32 ) * 5/9

    print(celcius_100) 
    print("float")
    # I know it is a float because it is origonally 37.77777777777778, when I print int the answer then becomes 37
convert_100_to_celsius()


def convert_0_to_celsius():
#     # Convert a temperature of 0 degrees fahrenheit to celsius
#     # Save this to a variable called celsius_0, and use print() to print out the value
    f = 0
    celcius_0 = ( f - 32 ) * 5/9
    
    print(celcius_0)
convert_0_to_celsius()

def convert_34_2_to_celsius():
    # Convert a temperature of 34.2 degrees fahrenheit to celsius
    # Do this one all in one print statement without saving any variables

    # f = 34.2
    # celcius_0 = ( f - 32 ) * 5/9
    # c = celcius_0
    # print(c)

    print((34.2 - 32) * 5/9)
convert_34_2_to_celsius()

# # '''
# # Now, can you convert back?
# # '''
# f = 34.2
# c= (f - 32) * 5/9
# print(f = (c * 9/5) + 32)
print((34.2 * 9/5) + 32)


def convert_5_to_fahrenheit():
#     # Convert a temperature of 5 degrees celsius to fahrenheit and print it out
    
    celcius = 5
    fahrenheit = (celcius * 9/5) + 32
    print(fahrenheit)
convert_5_to_fahrenheit()

def hotter_temp():
#     # What is hotter, a temperature of 30.2 degrees celsius, or a temperature of 85.1 degrees fahrenheit?
#     # Print out the hotter temp: '30.2 degrees celsius' or '85.1 degrees fahrenheit', respectively

    
    c = 30.2
    f = 85.1
    celcius = (f - 32) * 5/9
    fahrenheit = (c * 9/5) + 32
    print('30.2 degrees celsius')
    
    # print(fahrenheit > celcius)
    # print(fahrenheit - celcius)
hotter_temp()
