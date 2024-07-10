s = {12,12,4,1} # this is the way to Write Set
s  =() # This is a empty set but in order to add values in it you need to use  {} brackets

v ={12,5,5,5,5,"Hello",22.2}# This set contains repeated values (5 written 4 time) but Set will save 5 only one time
# Set can store Multiple datatype values like, Int, String, cant take boolean

print(v) # THis will only show 12,5 (5 will be printed only one time so in set values can't be repeated)
 
# We can use Sets when we don't want to repeat elements in a Program so we will use Set{}.

# Sets are Unordered, Unindexed(cannot access elements by index),Sets can't contain duplocate values, No way to change items
 

#______METHODS IN SETS_____________________#
#1 .add() Method we use this method to add new element in a Set.
v.add(590)
print(v)
#2 __len__() return the length of sets
print(v.__len__())
#3 Remove the element from the set
v.remove(590) # It will remove the 590 from set
print(v)
#4 v.pop() this will remove the specific element and in return it will give us that value which will removed
# print(v.pop(12))
#5 clear() this will clear the set and remove all values
# v.clear()
# print(v) # Empty set () will be prented
