# moodbot.py

from responses import get_motivation, get_daily_quotes, get_challenge

def main():
    print("Welcome to MoodBot! 🌈 Type 'quit' to exit.\n")

    # this will show dialy quotes from the jump
    print("Your Daily Boosts:")
    for quote in get_daily_quotes():
        print(f"- {quote}")
    print("\n")

    # the main loop for communicating
    while True:
        user_input = input("How are you feeling? ").lower()

        if user_input == 'quit':
            print("Goodbye! Stay positive! 🌟")
            break

        # show a motivational message
        print(get_motivation())

        # optional mini challenge
        print("Mini Challenge:", get_challenge())
        print("-" * 40)

if __name__ == "__main__":
    main()

