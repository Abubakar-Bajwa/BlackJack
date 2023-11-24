import random
from replit import clear

suits = ["spades", "hearts", "clubs", "diamonds"]
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cards_values = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}


def generateDeck():
    deck = []
    for suit in suits:
        for card in cards:
            deck.append((card, suit))
          
    random.shuffle(deck)
    return deck


def getCardValue(card):
    key = card[0]
    value = cards_values[key]
    return value


def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, dealer_score):

    if user_score > 21 and dealer_score > 21:
        return "You went over.  You lose"

    if user_score == dealer_score:
        return "Draw"
    elif user_score == 0:
        return "You got blackjack, you win"
    elif dealer_score == 0:
        return "Dealer got blackjack, you lose"
    elif user_score > 21:
        return "You went over 21, you lose"
    elif dealer_score > 21:
        return "Dealer went over 21, you win"
    elif user_score > dealer_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    user_cards = []
    dealer_cards = []
    user_score = []
    dealer_score = []
    game_over = False
    for x in range(2):
        user_cards.append(generateDeck().pop())
        dealer_cards.append(generateDeck().pop())

    for i in range(len(user_cards)):
        user_score.append(getCardValue(user_cards[i]))
        dealer_score.append(getCardValue(dealer_cards[i]))

    while not game_over:
        print(f"your cards are {user_cards}")
        print(f"dealers first card is {dealer_cards[0]}")
        print()
        player_Score = calculate_score(user_score)
        comp_score = calculate_score(dealer_score)
        print("your score is ", player_Score)
        print("Dealers first card value is ", dealer_score[0])

        if player_Score == 0 or comp_score == 0 or player_Score > 21:
            game_over = True
        else:
            more_cards = input(
                "Type 'y' to draw another card or type 'n' to pass: ")

            if more_cards == 'y':
                user_cards.append(generateDeck().pop())
                user_score.append(getCardValue(user_cards[-1]))
                player_Score = calculate_score(user_score)
            else:
                game_over = True

    while comp_score != 0 and comp_score < 17:
        dealer_cards.append(generateDeck().pop())
        dealer_score.append(getCardValue(dealer_cards[-1]))
        comp_score = calculate_score(dealer_score)

    print(f"Your hand: {user_cards}. \nYour final score: {player_Score}")
    print(f"Dealer hand: {dealer_cards}. \nDealer final score: {comp_score}")
    print()
    print(compare(player_Score, comp_score))


    while input("Type y to play again or n to stop ") == 'y':
      clear()
      play_game()

play_game()
