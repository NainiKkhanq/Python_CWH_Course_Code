
#_____LISTS IN PYTHON ________

friends = ['Apple', 'orange', 23,1,3,False]

print(friends[0])

# Changing the value in List (Lists are mutable) and it has collection of values with different data types
# List save values with Indexes and we can easily access the values using index you can add, delete or update list because its toally flexible
friends [0] = "Mango" # On index 0 i have Apple so i change it to Mango
print(friends[0])

#indexing in Lists....

print(friends[0:4]) # it will print the values from list from 0 to 4 index

# Methods for Lists: Google these methods according to your use.

#1: Append() method is used to add new value on new index

friends.append("Naini")

print(friends[0:])

#2: Sort() method (This method will sort the Numbers in list like if i write 0, 9, 8, 2 so it will change it to 0,2,8,9)
l1 =  [0,12,13,2,4,6,8,10,9]
l1.sort()
print(l1[0:])

#3: insert() This will add new value on the given index like inset(3,10) so it will add 10 on 3rd index

l1.insert(3,99) #It will add 99 on index 3
print(l1[0:])

#4: reverse() This will reverse the list 
l1.reverse()
print(l1[0:])

#5: pop() this will pop out the value from the specific index.And in returnn it will give us the removed value (in below case its 12).


print(l1.pop(1))
print(l1[0:])

#6 remove() This will take the value and than it will remove that value from the list (It will take value to remove not index)
l1.remove(0)
print(l1[0:])

#7 clear() it will clear the list
l1.clear() # This will return the Empty List.
print(l1[0:]) 