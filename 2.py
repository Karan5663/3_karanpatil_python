print("\n *******if statement***********")
var1=100
if var1==100:
    print("In if Statement")
    print(var1)
print("Outside if")
print("\n *****if-else statement*********")
var1=100
if var1:
    print("in if statement")
    print(var1)
else:
    print("in else statement")
print("\n *******short hand  statement*********")
var=100
if var==100:print("value is 100")
i=10
print("value is <15") if i<15 else print("value is >15")
print("\n ************elif statement************")
amount=int(input("enter the amount"))
if amount<1000:
      discount=amount*0.5
      print("discount:",discount)
elif amount<500:
      discount=amount*0.2
      print("discount:",discount)
else:
      discount=amount*0.1
      print("discount:",discount)
print("\n**************for loop**********")
l=["First",1,2,0]
for i in l:
    print(i)
print("\n**************continue*****************")
for l in "dypcetkop":
    if l=='e' or l=='p':
        continue;
    print("letter-",l)
print("\n**************Break*****************")
for l in "dypcetkop":
    if l=='e' or l=='p':
        break;
    print("letter is -",l)
print("\n**************pass*****************")
for l in "dypcetkop":
    pass
print("letter is -",l)
print("\n**************else with while*****************")
count=0
while count<5:
    print(count)
    count=count+1
else:
    print(count)
print("\n**************while loop*****************")
count=0
while count<4:
    count=count+1
    print("Karan R Patil")

a=[1,2,3,4]
while a:
    print(a.pop())
print("\n**************input*****************")
name=input("Enter name")
print(name)
num=int(input("Enter the number"))
print(num)
x,y,z=map(int,input("Enter Numbers").split())
print("The Number are ")
print(x,y,z)

l =list()
a=int(input("enter list size"))
print("Enter the element")
for i in range(0,a):
    l.append(int(input()))
print(l)


    







      


      

