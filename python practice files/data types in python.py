''' data types 
-Numeric integers,float,complex number
sequence type - string ,list,Tuple
dictionary
set  #Mutable data type(jiske andar kuch bhi update or chance kr skte h (list,Dictionary,byte array)
#immutable data types int,float ,comple,string,tuple,set (jiske anadar kuch changes nhi kr skte'''
#Number(integers,float,complex numbers)
a=5
print(a, type(a) )
a=5.5
print(a,type(a))
a=3+2j
print(a,type(a))

#string (collection value put in asingle and double quotion)
s='hqhkmz'      #"hjkl"          
'''gujhwd
eierd'''
print(s,type(s))
 
 #list[]  ordered sequence of items
l=['89','avi',80]
l[2]=8.5
print(l,type(l))

#tuple () ordered sequence of items same as a list tuple list se fast h tuple mai hmesha ek se jada value ane chaiye
t=(10,'sunita',23+8)
print(t,type(t))

#directory {} key:value unordered collection of key-value pairs
d={
    'Name':'avi',
    'course_duration' : '1 month'
}
print(d['course_duration'])
print(d,type(d))

#set {}unordered collection of items cannot be changed, unique value
s={10,20,40,20}
print(s,type(s))