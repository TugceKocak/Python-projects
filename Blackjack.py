import random

cards = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
deck = 52
list_card = list(cards.keys())

def add_card(num, card):
    card_play = []
    for i in range(0, num):
        card_play.append(random.choice(card))
    return card_play


def is_blackjack(card_user,card_dual):
    # When the game starts, there is only one condition to become a blackjack with two cards: the cards must be 'A' and '10'.
    card1_value = cards[card_user[0]]
    card2_value = cards[card_user[1]]
    user_blackjack=False
    if card1_value == 1 and card2_value == 10 or card1_value == 10 and card2_value == 1:
        user_blackjack=True

    card1_value = cards[card_dual[0]]
    card2_value = cards[card_dual[1]]
    dual_blackjack = False
    if card1_value == 1 and card2_value == 10 or card1_value == 10 and card2_value == 1:
        dual_blackjack = True

    if not user_blackjack and not dual_blackjack:
        return False
    print_hands(card_user,card_dual)
    print_winner(card_user,card_dual)
    return True

def total_value(card):
    total = 0
    for c in card:
        total += cards[c]
    if "A" in card and total < 11:
        total += 10
        return total
    else: return total


def less_than_21(num):
    if num <= 21:   return True
    return          False


def print_hands(user_hand, dual_hand):
    print(f"Your final hand: {user_hand}, final score: {total_value(user_hand)}")
    print(f"Computer's final hand: {dual_hand}, final score: {total_value(dual_hand)}")

def print_winner(com_total, user_total):

    if com_total > user_total:   return "Computer win 😭"
    elif user_total > com_total: return "You win 😃"
    else:                        return "Draw!"


def computer(total):
    if total <= 16: return "y"
    elif 16 < total < 21: return random.choice(["y", "n"])
    return "n"


def play_blackjack():
    want = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
    if want == "n": return

    if want == "y":
        # User
        user_cards = add_card(2, list_card)
        total_value_user = total_value(user_cards)
        print(f"Your cards: {user_cards}, current score: {total_value_user}")

        # Computer
        computer_cards = add_card(2, list_card)
        total_value_computer = total_value(computer_cards)
        print(f"Computer's first card: {computer_cards[1]}")

        if is_blackjack(user_cards,computer_cards):
            return play_blackjack()

        # add card
        is_less_user = less_than_21(total_value_user)
        while is_less_user:
            add = input("Type 'y' to get another card, type 'n' to pass:").lower()

            if add == "n": break
            elif add == "y":
                add_more = add_card(1, list_card)
                user_cards.append(add_more[0])
                total_value_user = total_value(user_cards)
                is_less_user = less_than_21(total_value_user)

                print(f"Your cards: {user_cards}, current score: {total_value_user}")
                print(f"Computer's first card: {computer_cards[1]}")


        is_less_computer = less_than_21(total_value_computer)
        while is_less_computer and is_less_user:
            com_choice = computer(total_value_computer)
            if com_choice == "y":
                add_more_com = add_card(1, list_card)
                computer_cards.append(add_more_com[0])
                total_value_computer = total_value(computer_cards)
                is_less_computer = less_than_21(total_value_computer)
            else: break

        print_hands(user_cards, computer_cards)
        if not is_less_user:
            print("You BUST. You lose 😭")
        elif not is_less_computer:
            print("Computer BUST. You win 😃")
        else:
            print(print_winner(total_value_computer, total_value_user))
        return play_blackjack()


play_blackjack()