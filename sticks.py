

player1 = input("What player name would you like to choose, player 1?")
print("Player 1 is named {}. ".format(player1))
player2 = input("What player name would you like to choose?")
print("Player 2 is named {}. ".format(player2))


# give initial number of sticks, then have number of sticks removed based on players' input

choice = int(input("What number of sticks would you like to start with? Please input a number between 10 & 100. "))
print("You have chosen {} sticks to start with.".format(choice))
if choice > 100 or choice < 10:
    print("Invalid selection. Please choose again. ")
#if turn_count = 0, then player one removed sticks, if turn_count = 1, then player2 removed sticks
def turn():
    if turn_count == 0:
        sticks_subtracted = int(input("Please select how many sticks you would like to remove, {}".format(player1)))
        print("{} has removed {} sticks. There are {} remaining.".format(player1, sticks_subtracted, sticks_remaining))
        turn_count += 1
    if turn_count == 1:
        sticks_subtracted = int(input("Please select how many sticks you would like to remove, {}".format(player2)))
        print("{} has removed {} sticks. There are {} sticks remaining.".format(player2, sticks_subtracted, sticks_remaining))
        turn_count -= 1

sticks_subtracted = int(input("Please select how many sticks you would like to remove."))
sticks_remaining = choice - sticks_subtracted
if 0 < sticks_subtracted < 4:
    print("There are {} sticks left.".format(sticks_remaining))
else:
    print("Please select between 1 and 3 sticks. ")


def enough_sticks():
    if sticks_remaining > 1:
        sticks_subtracted = int(input("Please select how many sticks you would like to remove."))
        sticks_remaining = sticks_remaining - sticks_subtracted
        print("There are {} sticks left,".format(sticks_remaining))
    return enough_sticks()

def end_of_game():
    if sticks_remaining == 1:
        print("There are {} sticks left. You lose.".format(sticks_remaining))
    elif sticks_remaining < 1:
        print("There are no sticks remaining. You lose.")








    #     print("Not a valid selection. Try again")


#removing sticks
# def remove_sticks:
#



# def player_names():
#     player_1 = input("What is your name, player 1? ")
#     player_2 = input("What is your name, player 2? ")
