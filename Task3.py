import cubed

number = input("Choose a number: ")

try:
    number_float = float(number)

    number_cubed = cubed.fun(number_float)

    print(number_cubed)

except Exception:
    print("Please select a number")
