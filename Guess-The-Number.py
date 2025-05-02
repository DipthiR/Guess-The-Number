import random
import time
import threading

def timeout():
    print("\nTime's up!")
    global time_out
    time_out = True

while True:
    print("\nNew game starting...")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    number = random.randint(1, 10)
    print("(Type 'exit' to quit)")

    for i in range(3):
        time_out = False

        # Start a timer for 5 seconds
        timer_thread = threading.Timer(5.0, timeout)
        timer_thread.start()

        user_input = input("Guess the number (1-10): ")

        # Cancel the timer if the user inputs within 5 seconds
        timer_thread.cancel()

        if user_input.lower() == "exit":
            print("Thanks for playing! Goodbye.")
            exit()  # Exits the program immediately

        if not user_input.isdigit():
            print("Please enter a valid number between 1 and 10 or 'exit' to quit.")
            continue

        user = int(user_input)

        if user == number:
            print(f"WOW! You guessed the number, and it's {number}.")
            break
        else:
            print("You guessed the wrong answer. Try again!")

    else:
        print(f"Sorry, you used all attempts. The number was {number}.")
