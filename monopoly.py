from random import randrange
from random import shuffle

player_names = []
player_money = []
player_properties = []
bank_properties = ["Mediterranean Avenue", "Baltic Avenue", "Oriental Avenue",
"Vermont Avenue", "Connecticut Avenue", "Charles Place", "States Avenue",
"Virginia Avenue", "St. James Place", "Tennessee Avenue", "New York Avenue",
"Kentucky Avenue", "Indiana Avenue", "Illinois Avenue", "Atlantic Avenue",
"Ventnor Avenue", "Marvin Gardens", "Pacific Avenue", "North Carolina Avenue",
"Pennsylvania Avenue", "Park Place", "Boardwalk", "Reading Railroad",
"Pennsylvania Railroad", "B. & O. Railroad", "Short Line", "Electric Company",
"Water Works"]
player_positions = []

def roll():
    d1 = randrange(1,7)
    d2 = randrange(1,7)
    
    #Determines value of roll and if doubles were rolled
    if d1 == d2:
        return [d1 + d2, True]
    else:
        return [d1 + d2, False]


def move(player):
    roll()
    roll = roll()
    print "Roll: %d" % roll[0]
    player_positions[player_names.index(player)] += roll[0]
    #location(player_positions[player_names.index(player)])
    
    if roll[1] == True:
        print "%s rolled doubles! Go again!" % player




def help(player):
    print "Commands: help, move, trade, mortgage, build, information."
    choice = raw_input("> ")
    directory(choice, player)


def directory(choice, player):
    if choice == "help":
        help(player)
    elif choice == "move":
        move(player)
    elif choice == "trade":
        trade(player)
    elif choice == "mortgage":
        mortgage(player)
    elif choice == "build":
        build(player)
    elif choice == "information":
        information(player)

def turn(player):
    print "It is %s's turn." % player
    directory(raw_input("> "), player)




def start():
    players_n = raw_input("How many players? (2-4) ")

    if int(players_n) > 4 or int(players_n) < 2:
        print "2-4 only."
        start()
    else:
        for n in range(1, int(players_n) + 1):
            name = raw_input("Player %d's name? " % n)
            player_names.append(name)
            player_money.append(1500)
            player_positions.append(0)

        print "Randomizing play order."
        shuffle(player_names)
        print "The order is as follows:"

        for n in range(0, len(player_names)):
            print player_names[n]

        turn(player_names[0])

start()
