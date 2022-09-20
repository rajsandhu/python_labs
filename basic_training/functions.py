# Function to calculate the highest of 2 numbers
def check_numbers(a, b):
    if a > b:
        return a
    else:
        return b

big_number = check_numbers(6, 65)

print(big_number)