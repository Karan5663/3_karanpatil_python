l1=[1,2,"hello",3.4]
print(type(l1))
print(l1[0: ])
print(l1[ : ])
print(l1[2:4])
print(l1[ :4])
print(l1[1:4:2])
print(l1[-1])
print(l1[-3:-1])
l1[2]=10
print(l1)
print("***************repetation************************")
l2=l1*2
print(l2)
print("***************Concatenation************************")
l3=l1+l2
print(l3)
print(len(l3))
print("***************iterating************************")
for l in l3:
    print(l)
print("***************membership************************")
print(1 in l1)
print("***************Adding element in list************")
l4=[]
n= int(input("enter no of element"))
for i in range (0,n):
    l4.append(input("enter the number"))
for i in l4:
    print(i,end=" ")
l4.remove(i)
print(l4)
print(len(l4))
print(min(l4))
print(max(l4))


