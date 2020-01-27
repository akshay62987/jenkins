s ="pyhton is ycuk"
s1=""
for i in s:
    s1=i+s1
print(s1)
print("---------")
print(s[::-1])
print("---------")
s2=s.split()
print(s2)
for i in s2:
    rev=""
    for j in i:
        rev=j+rev
    print(rev,end =" ")