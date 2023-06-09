#program to display the fibonacci series
#getting input from the user
n=int(input("ENTER THE NUMBER OF TERMS : "))
#first two terms
n1,n2=0,1
count=0
#condition
if n<=0:
    print("ENTER THE POSITIVE NUMBER")
#if they enter only one term
elif n==1:
    print("FIBONACCI SEQUENCE UPTO ",n)
    print(n1)
#generate fibonacci sequence
else:
    print("fibonacci sequence : ")
    while count<n:
        print(n1)
        nth=n1+n2
        #updating values
        n1=n2
        n2=nth
        count+=1
   
