# print the mix number





a=[]
n=int(input("enter the number of elements"))
for i in range(1,n+2):
    b=int(input("enter the number in list"))
    a.append(b)
a.sort()
print("2nd largest number is",a[n-1])
   
