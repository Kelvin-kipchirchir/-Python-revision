#!/usr/bin/env python
'''unordered collection of various items enclosed within a curly barackets and cannot be duplicated must be immutable'''
#creating using method 1
Days = {"Monday","Tuesday","wednesday","Thurday"}
print(Days)
print(type(Days))
print("-----looping through sets of elements-------")
for i in Days:
    print(i)

#creating using method 2
Days2 = set(["mon","tue","wed","thur"])
print(Days)

print("-----------sets operation----------------")
#iadding elements to a set
s = ([])
n = int(input("enter the number of elements want to put to set"))
for i in range(0,n):
    s.append(input("enter your items:"))
print("--printing items in a set---")
for i in s:
    print(i)

months = set(["jan","feb","march","april"])
print("printing the original set--:",months)
print("----adding elements to the set---")
months.add("August")
months.add("july")
print("now printing the modified set")
print(months)
for i in months:
    print(i)

#adding more elements
print(months)
print("updating the original list using update function")
months.update(["september","october","december"])
print("After modification we get",months)

#removing elements from the set
print("remving the elememts from the list")
months.discard("jan")
months.discard("feb")
print(months)

#removing using remove method
print("removing an element from the set")
me = input("input element you wish to remove from set")
if me in months:
    months.remove(me)
else:
    print("unknown value")
print("my lists is:",months)

#removing using pop method
print("current months list:",months)
months.pop()#removes the item at index 0
print("\nprinting the modified set",months)
months.pop()
print("printing the modified set again:",months)
#months.clear()-removes all elements in a list

#the key difference between discard and remove is that if key to be deleted from the set using discard() method doesn't exist in the set python will no give an error as program will maintain the flow.if items to be deleted from set using word remove() doesn't exist in the set
print(months)
print("\n removing items using the discard() method",months.discard("feb"))#will ignore if it finds no available item
print(months)
print("\nremoving items through remove() method")
#months.remove("january")#produces errors as key january is not available

#union of sets
Dys ={"mon","tue","wed"}
dys ={"sat","sun"}
print("combining the two sets",Dys.union(dys))

#intersecting the two sets to produce a common word present
set1 = {"kelvin","kipchirchir","kiplimo","kiptoo"}
set2 = {"brandon","muya","kiptoo","wanyama"}
print("the intersection of the two sets is:",set1&set2)
print("using an intersection word:",set1.intersection(set2))

#intersection update method:removes the items from the original set that are not present in both the sets
set3 = {"alice","bob","carol","kiptoo"}
set1.intersection_update(set2,set3)
print("the intersected_updated set becomes:",set1)

#difference of two sets
#can be calculated using the subtraction operand such that:
Dys = {"mon","tue","wed","thur"}
dys = {"mon","tue","sun"}
print("the difference of the two sets Dys and dys is:",Dys-dys)

#using the difference keyword
print("finding the difference between the two sets is:",Dys.difference(dys))

#difference_update() modifies the set by removing items that are also present in the specified set
print("finding the difference_update of the two sets",Dys.difference_update(dys))

#checking for a disjoint set
print("checking for a disjoint set:",Dys.isdisjoint(dys))

#summetric_difference_updates()-updates sets with a symmetric difference of itself and others
print("the summetric_difference_updates of the two sets above",Dys.symmetric_difference(dys))
print("the symmetric difference of set1 and set2 is:",set1.symmetric_difference(set2))

#set comparison
print("is Dys a superset of dys:should print true",Dys>dys)
print("is Dys a subset of dys:should print false",Dys<dys)
print("are the two subsets equal",Dys==dys)

'''
frozen set are immutable form of the normal sets ie the items of the frozen sets cannot be changed and therefore can be used as key in dictionary
frozenset() method is used to create a the frozen object.The iterable seq is passed into this method which is converted into frozen set

'''
frozenset = frozenset([1,2,3,4,5])
print(type(frozenset))
print("printing the contents of the frozen set")
for i in frozenset:
    print(i)
print("trying to add an item to the frozen set")
try:
    frozenset.add(6)
except:
    print("error can't add to a frozen set")

#frozensets for dictionary :if we pass the dictionary as the seq inside a frozenset(metho) it will take only the key from dictionary and return a frozen set that contains key 
Dict = {"Name":"John",
        "Country":"USA",
        "ID":101}
print(type(Dict))
#frozen = frozenset(Dict)
#print(type(frozen))
#for i in frozen:
#    print(i)







