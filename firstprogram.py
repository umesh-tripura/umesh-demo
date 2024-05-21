number = int(input("Enter a number:"))
sum = 0
order = len(str(number))
temp = number

while(number>0):
    digit =  number % 10
    sum += digit ** order
    number= number//10

if(sum == temp):
    print(f"{temp} is a armstrong number")
else:
    print(f"{temp} is not a armstrong number")
