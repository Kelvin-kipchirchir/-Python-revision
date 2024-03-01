#!/usr/bin/env python
print("doing some break and continue statements")
list1 = [1,2,3,4,5]
count = 1
for i in list1:
    if i==4:
        print("item matched")
        count=count+1
        break

print("found at:\t",count,"location")
#example2
str = "python"
for i in str:
    if i == "o":
        break
    print(i)

#example3
i=0
while i:
    print(i,"",end="")
    i=i+1
    if i == 10: 
        break
    print("coming out of a while loop")

#example4
n = 2
while i:
    i=1
    while i<= 10:
        print("%d*%d = %d\n"%(n,i,n*i))
        i=i+1
        choice = int(input("Do you wish to continue printing the table press 0 for the response:"))
        if choice == 0:
            break
n+=1

print("."*100)
print("printing a continue statement")
i=0
#while i!=10:
#while i<=10:
 #   print("%d"%i)
    #continue
    #uncommenting above will make it an endless loop
#i+=1

i=1
for i in range(1,11):
    if i== 5:
        continue
    print("%d"%i)

print("using the pass keyword")
for i in [1,2,3,4,5]:
    if i == 3:
        pass
        print("pass when value is:\t",i)
    print(i)


