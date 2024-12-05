
# Assignment 1: Write a program that prints all the odd numbers between variable A and variable B 


digit_a = int(input("Enter first number: "))
digit_b = int(input("Enter second number: "))

if digit_a < digit_b:
    while digit_a < digit_b:
        digit_a += 1
        if digit_a % 2 != 0 and digit_a != digit_b:
            print(digit_a)
            

elif digit_a > digit_b:
    digit_c = digit_a
    while digit_a > digit_b:
        if digit_a % 2 != 0 and digit_a != digit_c:
            print(digit_a)
        digit_a -= 1
else: 
    print("Error!")




# Question 2: write a program given a string "S" print all the even characters (in terms of the character count)

s = input("Enter a phrase or clause: ")
print(s[1::2])
