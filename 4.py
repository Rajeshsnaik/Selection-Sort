
# sort without using built-in functions

num = int(input("enter the numbers you want to enter : "))
list1=[int(input("enter number : ")) for x in range(num)]          #list compriation method
print("list is : ",list1)

for i in range(len(list1)-1):
    m_val=list1[i]
    for j in range(i+1,len(list1)):
        if list1[j] < m_val:                    #if we want to find in the descending value then change the sign.
            m_val=list1[j]
    
    m_ind = list1.index(m_val,i)
    if list1[i] != list1[m_ind]:
        list1[i],list1[m_ind]=list1[m_ind],list1[i]
print("Sorted list : " , list1)

# Output : 
# enter the numbers you want to enter : 5
# enter number : 2
# enter number : 77
# enter number : -1
# enter number : 5
# enter number : 0
# list is :  [2, 77, -1, 5, 0]
# Sorted list :  [-1, 0, 2, 5, 77]