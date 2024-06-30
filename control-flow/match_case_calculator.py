usernumber=int(input("Enter a number to see its multiplication table:"))
for i in range(1, 10 + 1):
    product = usernumber * i
    print(f"{usernumber} * {i} = {product}")