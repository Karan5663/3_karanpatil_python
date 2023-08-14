import array as arr
a=arr.array('i',[1,2,3])
print("new array")
for i in range (0,3):
    print(a[i],end=' ')
    
a1=arr.array('d',[2.5,1.5,3.5])
print('float array')
for i in range(0,3):
    print(a1[i],end=" ")

a.insert(1,4)
print(a)
print("*******************to insert at the end*************")
a.append(5)
for i in range (0,5):
    print(a[i],end=' ')
print("*******************to remove array*************")
a.remove(2)
print("*******************to delete the last element*************")
a.pop()
for i in range (0,len(a)) :
    print(a[i],end=' ')
print(a[3])
