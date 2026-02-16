import math

def main():
    print("Think of a number, and I will try to guess it.")
    
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    max_guesses = math.ceil(math.log(high - low + 1, 2))
    print(f"I must guess your number in no more than {max_guesses} guesses.")

    guesses_used = 0
    current_low = low
    current_high = high

    while current_low <= current_high:
        guess = (current_low + current_high) // 2
        guesses_used += 1

        print(f"My guess #{guesses_used}: {guess}")
        response = input("Is your number (h)igher, (l)ower, or (c)orrect? ").lower()

        if response == "c":
            print(f"I guessed your number in {guesses_used} guesses!")
            return

        elif response == "h":
            current_low = guess + 1

        elif response == "l":
            current_high = guess - 1

        else:
            print("Invalid response. Please enter h, l, or c.")
            guesses_used -= 1
            continue

        if current_low > current_high:
            print("\nIt seems your hints were inconsistent.")
            print("You may have changed your number or given misleading hints.")
            print("Game over.")
            return

        if guesses_used > max_guesses:
            print("\nYou forced me to exceed the minimum number of guesses.")
            print("This means your hints were misleading.")
            print("Game over.")
            return

    print("Something unexpected happened.")

if __name__ == "__main__":
    main()
