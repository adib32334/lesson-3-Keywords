#Break
a = str(input("Enter a word = "))
for i in a:
    if (i=="A"):
        print("A is Found")
        break
    else:
        print("A Not Found")
#Pass
for x in range(21):
    if (x % 20 ==0):
        print("Twist")
    elif (x % 15==0):
        pass
    elif (x % 5==0):
        print("Fizz")
    elif (x % 3==0):
        print("Buzz")
    else:
        print(x)
#Continue
c = 10
while c>0:
    if (c==5):
        continue
    print("\n I am ",c)
    c= c-1
print("\nGood bye")