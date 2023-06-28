Card_no = input("Enter Credit Card Number: ")

Card_no = Card_no[:: -1]
sum_odd_dig = 0
sum_even_dig = 0

for x in Card_no[::2]:
    sum_odd_dig += int(x)

for x in Card_no[1::2]:
    x = int(x) * 2
    if x>=10:
        sum_even_dig += 1 + (x%10)
    else:
        sum_even_dig += x

total = sum_odd_dig + sum_even_dig

if total%10 == 0:
    print("Valid")
else:
    print("Invalid")
