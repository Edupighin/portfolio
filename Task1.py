input_str = input("Type a number:")

try:
    input_int = int(input_str)
    print(input_int)

except Exception:
    print("Please type an integer.")
