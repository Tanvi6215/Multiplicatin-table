def table(n):
    for i in range(2,n+1):
        print("TABLE OF",i,":")
        for j in range(1,11):
            t=i*j
            print(i,'*',j,'=',t,end="")
            print()
        print()
m=int(input("Enter the number upto which the table should be printed: "))
table(m)
