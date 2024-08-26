s1 = {1, 2, 3, 4}
s2 = {1, 2, 5, 8, 9}

s3 = s1.union(s2)

print('union data : ',s3)

s4 = s1.intersection(s2)
print('intersection data : ',s4)

difference_set = s1.difference(s2)
print('difference data: ',difference_set)  # Output: {3, 4}

# Symmetric Difference
symmetric_difference_set = s1.symmetric_difference(s2)
print(symmetric_difference_set)  # Output: {3, 4, 5, 8, 9}