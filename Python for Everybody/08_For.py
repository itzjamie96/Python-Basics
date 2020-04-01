# FOR = definite loop
# - finite set of things
# - definite loops iterate through the members of a set
for i in [5,4,3,2,1] :
    print(i)
print('Blastoff!')


# Ex. finding the max num
nums = [3,41,12,9,74,15]
max = 0
for i in nums:
    if i>max:
        max = i
print(max)

# Ex. counting number of data in an array
nums = [3,41,12,9,74,15]
count = 0
for i in nums:
    count +=1
print(count)

# Ex. sum in loop
nums = [3,41,12,9,74,15]
sum = 0
for i in nums:
    sum +=i
print(sum)

# Ex. finding the avg
nums = [3,41,12,9,74,15]
for i in nums:
    sum += i
    count += 1
print(sum/count)

# Ex. filitering in a loop
nums = [3,41,12,9,74,15]
for i in nums:
    if i>20:
        print('bigger than 20')

# Ex. searching for a specific value
nums = [3,41,12,9,74,15]
found = False
for i in nums:
    if i==3:
        found = True
    else:
        found = False
    print(found, i)
print('finished')

# Ex. min
nums = [3,41,12,9,74,15]
min = None      #NULL 
for i in nums:
    if min == None:
        min = i
    elif i<min:
        min = i
print(min)

# "is" and "is not"
# - Similar to, but STRONGER THAN ==
# - "is not" is also a logical operator
# - DEMANDS EQUALITY
# - don't over use this
# - boolean & None