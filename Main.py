import random

class Card:

    def __init__(self, number = 1, suit = "Hearts"):
        self.number = number
        self.suit = suit

    def setacevalue(handvalue):
        total = handvalue + 11

        if total>21:
            return 1
        else:
            return 11

    def checkequal(self, card):
        if self.suit==card.suit and self.number==card.number:
            return True
        return False

    def assign(self, card):
        self.number = card.number
        self.suit = card.suit

    def printcard(self):
        print("{} of {}".format(self.number, self.suit))

class Deck:

    def __init__(self):
        self.deck = []

    def deckinit(self):
        suitcounter = ('hearts', 'spades', 'diamond', 'club')
        numbercounter = ('A',2,3,4,5,6,7,8,9,10,'J','Q','K')

        for currentsuit in suitcounter:
            for currentnumber in numbercounter:
                self.deck.append(Card(currentnumber, currentsuit))

    def printdeck(self):
        for card in self.deck:
            print("{} of {}".format(card.number, card.suit))

    def randomcard(self):
        return random.choice(self.deck)

    def indextocard(index):
        deck = Deck()
        deck.deckinit()
        return deck(index)

    def cardtoindex(card):
        index = 0
        deck = Deck()
        deck.deckinit()
        for cardtemp in deck.deck:
            if cardtemp.checkequal(card):
                return index
            index = index + 1

    def copydeck(deck1, deck2):
        index = 0
        for card in deck1:
            deck2[index] = Card(card.number, card.suit)
            index = index + 1

    def shuffle(self):
        shuffleddeck = []
        normaldeck = Deck()
        normaldeck.deckinit()

        for i in range(0,52):
            shuffleddeck.append(normaldeck.deck.pop(random.choice(range(0,(52-i)))))

        Deck.copydeck(shuffleddeck, self.deck)

class Hand:

    def __init__(self):
        self.hand = []
        self.value = 0

    def addcard(self, card):
        self.hand.append(card)
        value = 0
        try:
            if card.number == 'J' or card.number == 'Q' or card.number == 'K':
                value = 10
            elif card.number == 'A':
                value = Card.setacevalue(self.value)
            else:
                value = card.number

            self.value = self.value + value
        except:
            print("Hand value cannot be added. card.number = {}".format(card.number))

    def popcard(self):
        self.hand.pop()
        try:
            self.value = self.value - card.number
        except:
            print("A cannot be subtracted")

    def show(self):
        for card in self.hand:
            card.printcard()


class Player(Hand):

    def __init__(self, name, balance):
        Hand.__init__(self)
        self.name = name
        self.balance = balance
        self.wins = 0
        self.loses = 0
        self.bet = 0
        self.bustflag = False

    def betAction(self):

        while True:
            self.bet = int(input("You have ${}. How much would you like to bet?".format(self.balance)))
            if(self.balance>=self.bet):
                self.balance = self.balance - self.bet
                break
            else:
                print("You dont have enough funds.")


global name
global player
global gameflag

global dealerhand
global gamedeck
global hitflag
global winflag

def reset():
    #player
    while len(player.hand) > 0:
        player.hand.pop()
    player.value = 0
    player.bustflag = False

def gameengine():
    reset()
    hitflag = True
    winflag = False
    player.betAction()
    gamedeck = Deck()
    gamedeck.deckinit()
    gamedeck.shuffle()
    dealerhand = Hand()
    dealerhand.addcard(gamedeck.deck.pop())
    print("\nThe dealer has the following cards:")
    dealerhand.show()
    print("Faced down card")
    print("The total value of the dealer's hand is {} + the unknown value of the faced down card.".format(dealerhand.value))
    player.addcard(gamedeck.deck.pop())

    while hitflag:
        player.addcard(gamedeck.deck.pop())
        print("\n{}, you have the following cards:".format(player.name))
        player.show()
        print("The total value of the your hand is {}.".format(player.value))
        if player.value > 21:
            print("You have bust!")
            player.bustflag = True
            break
        hitstring = input("Would you like to hit or stand? (H/S)")
        if hitstring == 'S':
            hitflag = False
        else:
            hitflag = True

    if player.bustflag:
        winflag = False
    else:
        print("\nThe Dealer's turn.")
        while True:
            dealerhand.addcard(gamedeck.deck.pop())
            print("\nThe dealer has the following cards:")
            dealerhand.show()
            print("The total value of the dealer's hand is {}.".format(dealerhand.value))
            if dealerhand.value > 21:
                print("The dealer has bust!")
                winflag = True
                break
            elif dealerhand.value > player.value:
                print("The dealer won.")
                winflag = False
                break

    if winflag:
        print("\nYou won the round. Congrats.")
        player.balance = player.balance + player.bet + player.bet
        player.bet = 0
        player.wins = player.wins + 1
    else:
        print("\nYou lost the round. Better luck next time.")
        player.bet = 0
        player.loses = player.loses + 1



gameflag = True
print("Welcome to Captainspockear's Blackjack!")
name = input("\nWhat's your name?").title()
print("You will start off with a balance of $1000")
player = Player(name, 1000)
print("Your game will start now.")

while gameflag:

    gamestring = ''

    gameengine()

    if player.balance == 0:
        print("You have gone bankrupt.")
        gameflag = False
    else:
        gamestring = input("You have a balance of {}. Would you like to play again? (Y/N)".format(player.balance))
        if gamestring == 'N':
            gameflag = False

print("\nThanks for playing. Your stats:")
print("Number of wins: {}".format(player.wins))
print("Number of losses: {}".format(player.loses))
print("Your total points: {}".format(player.balance+(player.wins*300)-(player.loses*100)))