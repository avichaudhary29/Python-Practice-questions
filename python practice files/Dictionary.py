d = {123: 'avi', 21: 'Chaudhary', 555: 'ashu', '44': 'Kumar'}

# Loop through keys in the dictionary
for i in d:
    print(i)  # This prints the keys by default

# Loop through key-value pairs in the dictionary
for i, j in d.items():
    print(i, " ", j)  # This prints both the key and value

# Loop through sorted key-value pairs in reversed order
#for i, j in reversed(sorted(d.items())):
#    print(i, " ", j)

d.pop(555)
print(d)
d={'id':123,'name':'gaurav','last name':'Tomar','age':28,'salary':3000}
for i , j in d.items():
    print(i," ",j)

# for updation of any values in dictionary
d['salary']=50000
print(d)
d2={}
d2=d.copy()
print(d2)
d.clear()
print(d)

d=dict({1:'Wel',2:'col'})
print(d)

d = dict([(1,'Wel'),(2, 'sam'),(3,'Good')])
print(d) #list of tuples

d={'name':{ "first": "sam","last":"Gew"},"age":26,"pro":"student"}
print(d)
print(d['name']['first']) #accessing nested dictionary

# Define a dictionary containing data organized by categories
d = {
    'id': [1233, 44, 22],
    'name': ['gaurav', 'ravi', 'sachin'],
    'last name': ['tomar', 'garag', 'sharma'],
    'age': [12, 34, 53],
    'salary': [12000, 34500, 34500]
}

# Loop through the dictionary items (key-value pairs)
for i, j in d.items():
    # Print the current key (category) and its corresponding value (data)
    print(i, " ", j)
import pandas as pd

# Define the dictionary with data
'''import pandas as pd

# Define the dictionary with data
d = {
    'id': [1233, 44, 22],
    'name': ['gaurav', 'ravi', 'sachin'],
    'last name': ['tomar', 'garag', 'sharma'],
    'age': [12, 34, 53],
    'salary': [12000, 34500, 34500]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame(d)

# Print the DataFrame
print(df)

# Use setdefault to set a default value for a key
d.setdefault('age', 28)

# Print the modified dictionary
print(d)
'''
#user defined dictionary
'''x=int(input("Enter the dicitionary"))
d={}
for i in range(0,x):
    n1=eval(input("Enter the keys"))
    n2=eval(input("Enter the values"))
    d.setdefault((n1,n2))
print(d)'''
#dictionary comprehension
'''print({i: i**2 for i in range(1, 20)})
h = "avi chaudhary"
print({i: h.count(i) for i in h})
'''
'''
d={'id':2222,'name':'gaurav'}
d2={'salary':4444,'contact':3468348604}
d.update(d2)
print(d)'''

