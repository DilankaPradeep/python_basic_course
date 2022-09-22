
# list data structure
x = [12,15,25,30]
y = [0, 5, 10]


# Add values to list
# 1
x.append(100)
x.append(200)

# 2
x.insert(0, 1)

print(x)
# Remove element
# 1 element name
x.remove(12)
print(x)
# 2 element index
x.pop(0)
print(x)

# elements avaialability check (in operator)
print(15 in x)
is_15_not_in_x = 15 not in x;
print(is_15_not_in_x)


# add two lists
z = y + y
print(z)






