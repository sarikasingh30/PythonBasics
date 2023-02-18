# SETS

b = [8, 9, 0, 5, 3]
print(set(b))            # {0, 3, 5, 8, 9}

# Set store the data in the ordered form but not for negative integers, decimals
setA = [1, 9, -10, 7]
print(set(setA))        # {1, 7, 9, -10}

# so for that first sort the list
setA.sort()
print(setA)
