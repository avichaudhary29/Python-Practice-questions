t=(4,5,6,7,'gaurav','tomar','9444','899','gaurav','gaurav')
print(t[0])
print(t.count('gaurav'))
print(t.index('tomar'))
print(len(t))
#max is use when we have similar datatype
t=(4,5,6,7,8,9,12,34,556,65644,2342345)
print(max(t))
print(min(t))
print(sorted(t))
#nested tuple
t=("mouse",[8,4,6],[1,2,3])
print(t[0][3])
print(t[1][1])

t=(1,2)
print(t)
print(type(t))
t="hello"
print(type(t))

#tuple convert list and listto tuple

t=(4,5,6,'avi')
a=list(t)
print(a)
a=tuple(t)
print(a)
