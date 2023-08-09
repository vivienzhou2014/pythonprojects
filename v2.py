# Write your code below this line 👇
def prime_checker(number):
    if number == 1 or number == 2:
        print("It is a prime number.")
    else:
        num = number - 1
        while num > 1:
            if number % num != 0:
                num -= 1
            else:
                num = 0

        if num == 1:
            print("It's a prime number.")
        else:
            print("It's not a prime number")


# Write your code above this line 👆
# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
