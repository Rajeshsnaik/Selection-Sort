
# selection sort using max method(descending order)

list1=[20,23,44,5,1,22,3]

for i in range(len(list1)-1):
    max_val=max(list1[i:])
    max_index=list1.index(max_val)
    list1[i],list1[max_index]=list1[max_index],list1[i]
print(list1)

# Output :
# [44, 23, 22, 20, 5, 3, 1]