import random

def get_choice(choice):
    if choice == "D":
        return "đấm"
    elif choice == "K":
        return "kéo"
    elif choice == "L":
        return "lá"
    else:
        return "Not a valid choice"
def main():
    print("Welcome to my game")
    print("[D]=đấm, [K]=kéo, [L]=lá, [Q]=Quit Game")
    print("*"*40)

    choices = ["D", "K", "L"]
    counter = 1
    game_on = True

    while game_on:
        user_choice = input(f"Game #{counter}. Please center your choice: ")
        user_choice = user_choice.upper()

        if user_choice == "Q":
            print("Thanks for joining!")
            game_on = False
        else:
            random_index = random.randint(0, 2)
            computer_choice = choices[random_index]

            print(f"You selected -{get_choice(user_choice)}- "
                  f"vs Computer choice -{get_choice(computer_choice)}-")
            # winning rules:
            if user_choice == "D" and computer_choice == "K":
                print("Bạn thắng.")
            elif user_choice == "K" and computer_choice == "L":
                print("Bạn thắng.")
            elif user_choice == "L" and computer_choice == "D":
                print("Bạn thắng.")
            elif user_choice == computer_choice:
                print("Hòa nhé.")
            #lost
            elif user_choice == "D" and computer_choice == "L":
                print("Bạn thua.")
            elif user_choice == "K" and computer_choice == "D":
                print("Bạn thua.")
            elif user_choice == "L" and computer_choice == "K":
                print("Bạn thua.")
            else:
                print("Chỉ được nhập D, L, K.")
            counter += 1
        print("-"*40)
if __name__ == "__main__":
    main()
