import random


def createDeck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = []
    for suit in suits:
        for rank in ranks:
            if rank in ['Jack', 'Queen', 'King']:
                value = 10
            elif rank == 'Ace':
                value = 11  # Initially treat Ace as 11
            else:
                value = int(rank)
            deck.append((rank, suit, value))
    random.shuffle(deck)
    return deck


def dealCard(deck):
    if len(deck) > 0:
        return deck.pop()
    return None, None, None


def adjustAceValue(hand):
    for idx, card in enumerate(hand):
        if card[0] == 'Ace' and sum(card[2] for card in hand) > 21:
            hand[idx] = (card[0], card[1], 1)
    return hand


def playBlackjack():
    deck = createDeck()
    player1Hand = []
    player2Hand = []

    player1Bust = False
    player2Bust = False

    while deck and not (player1Bust and player2Bust):
        card1 = dealCard(deck)
        card2 = dealCard(deck)

        if card1:
            player1Hand.append(card1)
            player1Hand = adjustAceValue(player1Hand)
            if sum(card[2] for card in player1Hand) > 21:
                player1Bust = True

        if card2:
            player2Hand.append(card2)
            player2Hand = adjustAceValue(player2Hand)
            if sum(card[2] for card in player2Hand) > 21:
                player2Bust = True

        print(
            f"Player 1's hand: {[f'{card[0]} of {card[1]}' for card in player1Hand]} Total: {sum(card[2] for card in player1Hand)}")
        print(
            f"Player 2's hand: {[f'{card[0]} of {card[1]}' for card in player2Hand]} Total: {sum(card[2] for card in player2Hand)}\n")

        if player1Bust and player2Bust:
            print("Both players bust! No winner.")
        elif player1Bust:
            print("Player 2 wins!")
        elif player2Bust:
            print("Player 1 wins!")


if __name__ == "__main__":
    playBlackjack()
