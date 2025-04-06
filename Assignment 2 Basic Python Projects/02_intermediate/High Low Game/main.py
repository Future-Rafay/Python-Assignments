"""
Problem: High Low

We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and the way it's played goes as follows:

Two numbers are generated from 1 to 100 (inclusive on both ends): one for you and one for a computer, who will be your opponent. You can see your number, but not the computer's!

You make a guess, saying your number is either higher than or lower than the computer's number

If your guess matches the truth (ex. you guess your number is higher, and then your number is actually higher than the computer's), you get a point!

"""

import random

NUM_ROUNDS = 5


def main():
    print("🎉 Welcome to the High-Low Game! 🎉")
    print('----------------------------------------')
    score = 0

    for i in range(NUM_ROUNDS):
        computer_num = random.randint(1, 100)
        user_num = random.randint(1, 100)

        if i + 1 == NUM_ROUNDS:
            print(f"\n🎯 Final Round {i + 1}")
        else:
            print(f"\n🎮 Round {i + 1}")

        print(f"🔢 Your number is: {user_num}")

        while True:
            try:
                user_choice = input(
                    "🤔 Do you think your number is higher or lower than the computer's? (h/l): ").lower()

                if user_choice in ("l", "lower"):
                    if user_num < computer_num:
                        score += 1
                        print(
                            f"✅ You were right! 🎉 The computer's number was {computer_num}")
                    else:
                        print(
                            f"❌ Oops! The computer's number was {computer_num}")
                    break

                elif user_choice in ("h", "higher"):
                    if user_num > computer_num:
                        score += 1
                        print(
                            f"✅ You were right! 🎉 The computer's number was {computer_num}")
                    else:
                        print(
                            f"❌ Oops! The computer's number was {computer_num}")
                    break

                else:
                    print(
                        "🚫 Invalid input. Please type 'h' for higher or 'l' for lower.")

            except (KeyboardInterrupt, EOFError):
                print("\n⚠️ Game interrupted. Exiting...")
                return

        print(f"📊 Your Score so far: {score}/{i + 1}")

    print("\n🏁 Game Over!")
    print(f"🎯 Final Score: {score}/{NUM_ROUNDS}")

    # 🎓 Final performance evaluation
    if score == NUM_ROUNDS:
        print("🌟 Perfect game! You're a High-Low Master! 🧠🏆")
    elif score >= 3:
        print("👏 Great job! You’ve got some solid guessing skills! 💪😎")
    elif score >= 1:
        print("😅 Not bad! Keep practicing and you'll get better! 🔁")
    else:
        print("😢 Oh no! That was rough. Better luck next time! 🍀")


if __name__ == "__main__":
    main()
