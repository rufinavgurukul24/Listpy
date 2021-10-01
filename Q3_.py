# List product excluding duplicates.
#     List = [6,1,3,5,6,3,1]
#     Output: 60

list1=[6,1,3,5,6,3,1]
i=0
# sum=0
s=[]
while i<=len(list1):
    a=list1[i]
    if a not in s:
        s.append(a) 
        i=i+1
    print(s)