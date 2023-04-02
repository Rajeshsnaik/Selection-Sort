
# in a proper manner.

list1=[20,23,44,5,1,22,3]

for i in range(len(list1)-1):
    min_val=min(list1[i:])
    min_index=list1.index(min_val)
    if list1[i] != list1[min_index]:
        list1[i],list1[min_index]=list1[min_index],list1[i]
    print(list1)

# Output : 
# [1, 23, 44, 5, 20, 22, 3]
# [1, 3, 44, 5, 20, 22, 23]
# [1, 3, 5, 44, 20, 22, 23]
# [1, 3, 5, 20, 44, 22, 23]
# [1, 3, 5, 20, 22, 44, 23]
# [1, 3, 5, 20, 22, 23, 44]