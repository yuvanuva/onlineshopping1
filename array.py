import array as arr  
a = arr.array('i', [2, 4, 6, 8])
print("First element:", a[0])  
print("Second element:", a[1])  
print("Second last element:", a[-1])
a[0]=0
print(a[0])
