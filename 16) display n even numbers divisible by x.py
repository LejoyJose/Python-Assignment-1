start=int(input("Enter the starting value :"))
total=int(input("Enter the total number :"))
divisible=int(input("Enter the divisible number :"))
count=0

while(count<total):
    if (start%divisible==0):
        print(start,end=" ")
        count+=1
    start+=1

    
