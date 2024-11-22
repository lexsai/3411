
text = input("enter isbn:")
err_digit = int(input("enter digit:"))

isbn_digits = [int(x) if x != 'X' else 10 for x in text if x != '-']

# isbn_digits = [9,8,7,3,0,8,4,8,5,8]
if len(isbn_digits) != 10:
    print("error! invalid isbn")

for i in range(0, 10):
    isbn_digits[err_digit - 1] = i

    print(isbn_digits)

    total = 0
    for j, x in enumerate(isbn_digits):
        total += (j + 1) * x

    print(total, total % 11)

    if total % 11 == 0:
        print("solution found!", i)
