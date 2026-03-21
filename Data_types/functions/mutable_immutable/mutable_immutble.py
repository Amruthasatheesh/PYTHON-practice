x = "hello"
y = x
y = y.upper()
print(x)#hello
# what will be the output
x = [1, 2]
y = x
y = y + [3]
print(x)
#what will be the output
def modify(lst):
    lst.append(100)

x = [1, 2, 3]
modify(x)
print(x)
#predict output
def modify(x):
    x = x + 10

a = 5
modify(a)
print(a)
#shallow copy
x = [[1, 2], [3, 4]]
y = x.copy()
y[0][0] = 100
print(x)#[[100, 2], [3, 4]] shallow copy only applicable for outer objects only,so the change on y is also to x tooo
# Write a function that:

# Takes a list
# Modifies it by adding an element
# Returns the same list
def lst_fun(x):
    x.append(10)
    return x
print(lst_fun([1,2,3,4]))

# Write a function that:
# Takes a tuple
# Returns a new tuple with one extra element
def tup_fun(x):
    res=x+(4,)
    return res
print(tup_fun((1,2,3)))

#chk an object is mutable or immutable
def chk_obj(object):
    if isinstance(object,(list,set,tuple)):
        return "mutable"
    else:
        return "immutable"
print(chk_obj([1,2,3,4]))#mutable
print(chk_obj({1,2,3,4}))#mutable
print(chk_obj((1,2,3,4)))#immutable
