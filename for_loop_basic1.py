#Print integers from 0 to 150
for x in range(0,151):
    print(x)

#Print all the multiples of 5 from 5 to 1,000
for m in range(5,1001):
    if m % 5 == 0:
        print(m)

#Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for m in range(1,101):
    if m %10 == 0:
        print("Coding Dojo")
    elif m % 5== 0:
        print("Coding")
    else:
        print(m)

#Add odd integers from 0 to 500,000, and print the final sum.
sum=0
for i in range(1,500000,2):
    sum += i
    if i>=500000:
        print(sum)

        sum = 0
for i in range(1,500001,2):
    sum += i
print(sum)


# Print positive numbers starting at 2018, counting down by fours.
for pn in range(2018,0,-4):
    print(pn)

# Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
lowNum=2
highNum=9
mult=3
for i in range(lowNum,highNum+1):
    if i % mult == 0:
        print(i)