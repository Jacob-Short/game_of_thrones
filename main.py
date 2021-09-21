import os 

def main():
    # game loop
    while True:
        try:
            os.system('clear')
            choice = game_menu()
            if choice.lower() == 'q':
                break
        except Exception as err:
            print(err)

def game_menu():
    print('Main Menu')
    print('1. Login')
    print('2. Create an account')
    print()
    choice = input("Select an option ('q' to quit ):")

    return choice


if __name__ == '__main__':
    main()