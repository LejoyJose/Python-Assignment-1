start=int(input("Enter the starting value :"))
end=int(input("Enter the ending value :"))
divisible=int(input("Enter the value :"))
count=0
for i in range(start,end+1):
    if(i% divisible==0):
        count+=1
print(count,end=" ")
