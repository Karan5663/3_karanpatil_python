d1={1:"hello",2:"hi",3:"welcome"}
print("********************print key********************")
print(d1.keys())
print("********************print values********************")
print(d1.values())
print("********************print key values********************")
print(d1.items())
print("********************to get key values********************")
print(d1.get('a'))
print("********************to create copy of dictionary********************")
newd=d1.copy()
print(newd)
print("********************removes specific elements********************")
print(d1.pop(1))
print(d1)
print("********************removes last element********************")
print(d1.popitem())
print(d1)
print("********************to add data ********************")
d2={4:"welcome"}
d1.update(d2)
print(d1)
print("********************declear the dictionary********************")
d1.update({5:"Hi"})
d1.clear()
print(d1)
d3={'a','b','c','d'}
d4=dict. fromkeys(d3,1)
print(d4)
