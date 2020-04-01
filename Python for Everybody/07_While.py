n=5
while n>0:  # is n greater than 0?
    print(n)    #if yes, print n
    n = n-1     #then n-1
print('Blasoff!')   #if !n>0, print this
print(n)

# Breaking out of a loop
while True:
    line = input('write a line: ')
    if line == 'done':
        break
    print(line)
print('done!')

# continue
# - go up back to the top of the loop
while True:
    line = input('write a line: ')
    if line[0] =='#':
        continue        #if input=='#' -> go back to the while True:
    if line == 'done':
        break
    print(line)
print('Done!')

# WHILE = indefinite loop
# - loops that keep going until a logical condition becomes false