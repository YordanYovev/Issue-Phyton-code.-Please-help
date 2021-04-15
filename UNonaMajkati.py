#generate UNO deck of 108cards
# The deck consists of 108 cards: four each of "Wild" and "Wild Draw Four,"
# and 25 each of four different colors (red, yellow, green, blue).
# Each color consists of one zero, two each of 1 through 9, and two each of
# "Skip," "Draw Two," and "Reverse."
# These last three types are known as "action cards."


import random



def main():
    class Card(object):
        def __init__(self, value, colour):
            self.value = value
            self.colour = colour

        def __repr__(self):
            value_name = ""
            colour_name = ""


            #value
            if self.value == 0:
                value_name = "0"
            if self.value == 1:
                value_name = "1"
            if self.value == 2:
                value_name = "2"
            if self.value == 3:
                value_name = "3"
            if self.value == 4:
                value_name = "4"
            if self.value == 5:
                value_name = "5"
            if self.value == 6:
                value_name = "6"
            if self.value == 7:
                value_name = "7"
            if self.value == 8:
                value_name = "8"
            if self.value == 9:
                value_name = "9"
            if self.value == 10:
                value_name = "Draw Two"
            if self.value == 11:
                value_name = "Skip"
            if self.value == 12:
                value_name = "Reverse"


                #colours
            if self.colour == 0:
                colour_name = "Red"
            if self.colour == 1:
                colour_name = "Green"
            if self.colour == 2:
                colour_name = "Yellow"
            if self.colour == 3:
                colour_name = "Blue"


            return value_name + " " + colour_name

    class SpecialCards(object):
        def __init__(self,wild,wildSpecial):
            self.wild = wild
            self.wildSpecial = wildSpecial
        def __repr__(self):
            wild_name = ""
            wildSpecial_name = ""


            #value
            if self.wild == 0 or 1 :
                wild_name = "Wild"
            if self.wildSpecial == 0:
                wildSpecial_name = "_Draw Four"
            if self.wildSpecial == 1:
                wildSpecial_name = "_"
            if self.wildSpecial == 2:
                wildSpecial_name = "_Draw Four"
            if self.wildSpecial == 3:
                wildSpecial_name = "_"

            return wild_name + wildSpecial_name



    class StandardDeck(list):
        def __init__(self):
            super().__init__()
            colours = list(range(4))
            values = list(range(13))
            wilds = list(range(2))
            wildSpecials = list(range(4))
            # [[self.append(Card(i, j)) for j in colours] for i in values]
            for value in values:
                for colour in colours:
                    self.append(Card(value,colour))
                    self.append(Card(value,colour))
            for wild in wilds:
                for wildSpecial in wildSpecials:
                    self.append(SpecialCards(wild,wildSpecial))


    deck = StandardDeck()
    ImShureThereIsBetterWay = []


    def drawCards (numCards):
        cardsDrawn =[]
        for x in range (numCards):
            cardsDrawn.append (deck.pop(0))
        return cardsDrawn

    ImShureThereIsBetterWay.append(drawCards(4))

    # random.shuffle(deck)
    # for card in deck:
    #     print(card)
    discard = []
    discard.append(drawCards(1))
    print(discard)

    def showHand(player,playerHand):
        print("player {}".format(player+1))
        print("Your hand:")
        print("-------------------")
        y=1
        for card in playerHand:
            print("{}) {}".format(y, card))
            y +=1
        print("-------------------")

    players = []
    numPlayers = int(input("How many players?"))

    while numPlayers <2 or numPlayers>4:
        numPlayers = int(input("Invalid!!! Plaese enter number between 2-4.How many players?"))
    for player in range(numPlayers):
        players.append(drawCards(5))

    playerTurn = 0
    playDirection = 1
    playing = True
    # discard.append(deck.pop(0))
    # splitCard = discard[0].split(" ",1)
    # currentColour = splitCard[0]


# while playing:
#     showHand(playerTurn,players[playerTurn])
#     print("Card on the top of discard deck: {}".format(discard[-1]))
#     if canPlay(currentColour,cardVal,players[playerTurn]):
#         cardChosen = int(input("Which card do you want to play?"))
#         while not canPlay(currentColour,cardVal,[players[playerTurn][cardChosen -1]]):
#             cardChosen = int(input("Not a valid card.Which card do you want to play?"))
    # ******
# def canPlay(colour,value,playerHand):
#     for card in playerHand:
#         if "Wild" in card:  #splitCard[-1]:
#             return True
#         elif colour in card or value in card:
#             return True
#     return False
# ****
    # rrr =discard[-1]
    # def playable():
    #     if rrr=="0 Yellow" and cardChosen=="0 Blue":
    #         return True
    #     else:
    #         return False


    # def canPlay(Card,playerHand):
    #     for card in playerHand:
    #         if "Wild" in card:
    #             return True
    #         # elif playable:
    #         #     return True
    #     return False

    def canPlay():
        if discard[-1]== "0 Yellow":
            if "Wild" or "0" or "Yellow" in cardChosen:
                return True
            else:
                False

    while playing:




        showHand(playerTurn,players[playerTurn])
        print("Card on the top of discard deck: {}".format(discard[-1]))
        if canPlay:
            cardChosen = int(input("Which card do you want to play?"))
            while not canPlay:
                cardChosen = int(input("Not a valid card.Which card do you want to play?"))
            print("You played : {}".format(players[playerTurn][cardChosen -1]))
            print("*****")
            discard.append(players[playerTurn].pop(cardChosen-1))

        else:
            print("You cant play. You have to draw a card")
            players[playerTurn].extend(drawCards(1))

        playerTurn += playDirection
        if playerTurn >= numPlayers:
            playerTurn = 0
        elif playerTurn < 0:
            playerTurn = numPlayers -1


    discard[-1].split
    print(discard[-1])



main()