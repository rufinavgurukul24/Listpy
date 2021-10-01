# count the element that which is smaller then 20 and bigger then 40


num=[50, 40, 23, 70, 56, 12, 5, 10, 7]
b=[]
count=0
i=0
while i<len(num):
    a=num[i]
    if a>20 and a<40:
        b.append(a)
        count=count+1
    i=i+1
print(b,count)  











