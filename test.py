a = [1,2,3]
b = [4,5,6]
c = []

for i,j in zip(a,b):
    c.append(i*j)
    
print(c)