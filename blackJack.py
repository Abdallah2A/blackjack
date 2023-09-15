import random

def calculate_score(cards):
    return sum(cards)

def pick_card(cards):
    return random.choice(cards)

def my_turn(cards, my_cards):
    while True:
        my_cards.append(pick_card(cards))
        check = calculate_score(my_cards)
        print(f"My cards {my_cards} = {check}")
        
        if check == 21:
            print("You got 21!")
            break
        
        if check > 21 and 11 in my_cards:
            index = my_cards.index(11)
            my_cards[index] = 1
            check = calculate_score(my_cards)
        
        if check > 21:
            print("You busted!")
            break
        
        # Prompt user for input until they provide 'y' or 'n'
        while True:
            choice = input("Do you need one more card? (y/n): ").lower()
            if choice == 'y' or choice == 'n':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        
        if choice == 'n':
            break

def pc_turn(cards, pc_cards, my_cards):
    while True:
        pc_cards.append(pick_card(cards))
        check = calculate_score(pc_cards)
        print(f"PC cards {pc_cards} = {check}")
        
        if check == 21:
            print("PC got 21!")
            break
        
        if check > 21 and 11 in pc_cards:
            index = pc_cards.index(11)
            pc_cards[index] = 1
            check = calculate_score(pc_cards)
        
        if check > 21 or (check > calculate_score(my_cards) and calculate_score(my_cards) <= 21):
            break

def check_the_winner(my_cards, pc_cards):
    my_score = calculate_score(my_cards)
    pc_score = calculate_score(pc_cards)
    
    if my_score == 21 and len(my_cards) == 2:
        print("BLACKJACK! YOU ARE THE WINNER")
    elif pc_score == 21 and len(pc_cards) == 2:
        print("BLACKJACK! YOU ARE LOOOOOSSSEEER")
    elif (my_score > pc_score and my_score <= 21) or (pc_score > 21 and my_score <= 21):
        print("You are the winner")
    elif my_score == pc_score:
        print("It's a draw")
    else:
        print("You are the loser")

while True:
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    print("Welcome to blackjack game")

    my_cards = [pick_card(cards)]
    pc_cards = [pick_card(cards)]

    print(f"PC cards [{pc_cards[0]}, *]")

    my_turn(cards, my_cards)
    pc_turn(cards, pc_cards, my_cards)
    check_the_winner(my_cards, pc_cards)

    # Prompt user for input until they provide 'y' or 'n'
    while True:
        play_again = input("Do you want to play again? (y/n): ").lower()
        if play_again == 'y' or play_again == 'n':
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    
    if play_again == 'n':
        break
