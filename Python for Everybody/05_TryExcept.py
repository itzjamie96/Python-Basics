#Try/ Except
# Try A, and if it doesn't work, just do Except: B
# If A works, ignore the Except clause

astr = 'Hello Bob'
try:
    istr = int(astr)    #doesnt' work
except:
    istr = -1      

print('First', istr)

astr='123'
try:
    istr=int(astr)
except:
    istr = -1

print('Second', istr)