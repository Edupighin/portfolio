number_list = [12, 45, 13, 11, 1, 4, 5]

while True:
    number = input("Guess a number: ")

    if number == "q":
        break

    try:
        number_int = int(number)

        if number_int in number_list:
            print("Well done!")

        else:
            print("Sorry, try again.")

    except Exception:
        print("Please type an integer or q to quit.")
