# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]



a=[]
n=int(input("enter the number of elements"))
for i in range(1,n+1):
    b=int(input("enter the number in list"))
    a.append(b)
a.sort()
print("second hightest number is",a[n-2])



   