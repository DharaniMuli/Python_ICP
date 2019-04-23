rev = 0
number = int(input("Enter any 3 digit number: "))
while number > 0:
    lastNumber = number % 10
    rev = rev*10+lastNumber
    number = number // 10

print(rev)
