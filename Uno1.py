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