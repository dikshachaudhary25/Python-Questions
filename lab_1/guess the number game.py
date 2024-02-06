a=38
count=0
while i<100:
    count+=1
    num=int(input("enter a guessed num: "))
    if(num>a):
        print("Higher num guessed")
    elif(num<a):
        print("Lower num guessed")
    elif(num==a):
        print("Guessed the number")
        break
print("Total number of attempts: ",count) 
