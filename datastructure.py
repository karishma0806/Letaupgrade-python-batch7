#LIST
l=[12,34,45,67,78,99]
l.append(122)    #APPEND()
print(l)

print(l[2:5])    #SLICE()

print(l*4)       #REPLICATING

print(l.pop(5))  #POP()

l.remove(34)     #REMOVE()
print(l)

l.insert(3,500)   #INSERT()
print(l)

del l[0]         #DELETE()
print(l)

print(max(l))   #MAXMIUM()

print(min(l))   #MINIMUM

print(len(l))   #LENGTH()

l.reverse()     #REVERSE()
print(l)

l.sort()        #SORT()
print(l)


#DICTIONARY


d={'name':'ammi','surname':'patan','nickmame':'ammijan'}
print(d)
print(d.keys())      
print(d.values())
print(d.items())

d["name"]="abida"    #UPDATE()
print(d)

print(len(d))          #LENGTH()

b=d.copy()             #COPY()
print(b)

d.clear()             #CLEAR()
print(d)


#SETS
s={'a','b','c','d'}
u={'e','h','c','l',}

s.discard('b')       #DISCARD
print(s)

s.add("IT")          #ADD
print(s)

a=s|u                #UNION
print(a)

a=s&u              #INTERSECTION
print(a)

p=s-u              #DIFFERENCE OF SETS
print(p)

c=s<=u             #COMPARE SETS
print(c)
c=u<=s
print(c)


#TUPLE
l=(12,34,56,788,77,89)
print(l)

print(l[3:])     #SLICE

print(len(l))    #LENGTH

print(min(l))    #MINIMUM

print(max(l))    #MAXIMUM

print(l*2)       #REPLICATING


#STRING
a="letsupgrade"
b="challange"
print(a+b)            #ADDING STRINGS()

print(a[4:])          #SLICE()

c=b.index("a")        #INDEX()
print(c)

d="l"
print(b.count(d))      #COUNT()

print(a.isalpha())     #ALPHANUMERICAL

print(b.isalnum())

print(b.isdigit())

print(b.capitalize())      #CAPITALIZE 

print(a.swapcase())












