# def : define function
# def name():
# - just creates and records the function
# - no running!
# - to reuse same things that happen again and again
# - a fucntion is some stored code that we can use
def thing():
    print('Hello')
    print('Fun')

thing()
print('Zip')
thing()

# Hello
# Fun
# Zip
# Hello
# Fun

############################################
# Built in functions

# Max : return biggest character
big = max('Hello world')
print(big)  # w

# Min : return smallest character
tiny = min('Hello world')
print(tiny) # (empty space)

##############################################
# Return
def greet():
    return "Hello"

print(greet(), "Jamie")

###############################################
## Parameter and Argument
def add(a, b):  #a, b = parameter
    return a+b

print(add(1,2)) #1, 2 = argument