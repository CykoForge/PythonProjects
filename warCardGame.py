import random

def war():
    player_cards = 26
    computer_cards = 26
    
    while player_cards > 0 and computer_cards > 0:
        play_card = input("Type y to place a card: ")
        if play_card.lower() == "y":
            cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
            player_draw = random.choice(cards)
            computer_draw = random.choice(cards)
            
            def card_display(card):
                if card == 11:
                    return "J"
                elif card == 12:
                    return "Q"
                elif card == 13:
                    return "K"
                elif card == 14:
                    return "A"
                else:
                    return str(card)
            
            player_display = card_display(player_draw)
            computer_display = card_display(computer_draw)
            
            print(f"You drew a {player_display}")
            print(f"The computer drew a {computer_display}")
            
            if player_draw > computer_draw:
                player_cards += 1
                computer_cards -= 1
                print("You win this round!")
            elif player_draw < computer_draw:
                player_cards -= 1
                computer_cards += 1
                print("The computer wins this round!")
            else:
                print("It's a tie!")
            
            print(f"You have {player_cards} cards left")
            print(f"The computer has {computer_cards} cards left")
        else:
            break
    
    if player_cards == 0:
        print("The computer wins the game!")
    elif computer_cards == 0:
        print("You win the game!")
    else:
        print("Game over!")
        
    return
            
        
