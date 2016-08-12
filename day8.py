lst = [1, 2, 3, 4]
var = " ".join(str(item) for item in lst) # change to a str

# change back to a list of strings
var.split()

# change to a list of ints
[int(x) for x in var.split()]

a = lst[:]

# deleting an element
a.pop()
a.remove(1)
del a[0]
b.pop(0)


lst = ["A", "BCA", "AB"]
print(sorted(lst))

lst2 = [(1,2), (1,0,0), (1,2,3,5)]
# the return value of len is the sorting key
print(sorted(lst, key=len)) 

def sum_last_two(lst):
    return sum(lst[-2:])
    
dict(sape="blah",apple="blah2",x="blah3")

def reverse_lookup(dictionary, value):
    d = {}
    
    return key_or_keys