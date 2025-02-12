a = [1, -10, 42, 5]
min_1 = a[0]
min_2 = a[1]
for x in a:
    if x < min_1: 
     min_2 = min_1
     min_1 = x 
print(min_1, min_2)