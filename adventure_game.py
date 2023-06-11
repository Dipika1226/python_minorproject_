import random

def start_game():
    print("Welcome to the Adventure Game!")
    print("You wake up in a mysterious room with two doors.")
    print("What do you do?")
    print("1. Go through the left door.")
    print("2. Go through the right door.")

    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        go_left()
    elif choice == "2":
        go_right()
    else:
        print("Invalid choice. Please try again.")
        start_game()

def go_left():
    print("You enter a dark hallway.")
    path = random.randint(1, 3)  

    if path == 1:
        encounter_monster()
    elif path == 2:
        find_treasure()
    elif path == 3:
        continue_exploring()
    else:
        print("Something went wrong. Please try again.")
        start_game()

def encounter_monster():
    print("You encounter a monster. Game over!")

def find_treasure():
    print("You find a hidden treasure. Congratulations, you win!")

def continue_exploring():
    print("You continue exploring the hallway.")
    options = [
        "You discover a secret room with valuable artifacts. Congratulations, you win!",
        "You trigger a hidden trap and get caught. Game over!",
        "You find a locked chest. Try to pick the lock? (y/n): "
    ]
    outcome = random.choice(options)

    if outcome == options[0]:
        print(outcome)
    elif outcome == options[1]:
        print(outcome)
    elif outcome == options[2]:
        choice = input(outcome)
        if choice.lower() == "y":
            pick_lock()
        elif choice.lower() == "n":
            print("You leave the chest and continue your exploration.")
        else:
            print("Invalid choice. Please try again.")
            continue_exploring()

def pick_lock():
    print("You successfully pick the lock and find a valuable treasure. Congratulations, you win!")

def go_right():
    print("You find yourself in a room with a locked door.")
    print("There is a key on a table.")
    choice = input("Do you take the key? (y/n/secret): ")

    if choice.lower() == "y":
        unlock_door()
    elif choice.lower() == "n":
        search_another_way()
    elif choice.lower() == "secret":
        enter_secret_code()
    else:
        print("Invalid choice. Please try again.")
        go_right()

def unlock_door():
    print("Congratulations! You unlocked the door and escaped. You win!")

def search_another_way():
    print("You search for another way out.")
    options = [
        "You find a hidden passage and escape. Congratulations, you win!",
        "You discover a trapdoor that leads to freedom. Congratulations, you win!",
        "You stumble upon a secret tunnel and make your way out. Congratulations, you win!",
        "You try to break down a wall, but it collapses on you. Game over!"
    ]
    outcome = random.choice(options)
    print(outcome)

def enter_secret_code():
    print("You notice a small panel with a keypad.")
    code = input("Enter the secret code: ")

    if code == "12345":
        print("The door unlocks, and you escape to safety. Congratulations, you win!")
    else:
        print("The alarm goes off, and you get caught. Game over!")

start_game()
