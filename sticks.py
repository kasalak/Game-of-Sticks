

player1 = input("What player name would you like to choose, player 1?")
print("Player 1 is named {}. ".format(player1))
player2 = input("What player name would you like to choose?")
print("Player 2 is named {}. ".format(player2))


# give initial number of sticks, then have number of sticks removed based on players' input
choice = int(input("What number of sticks would you like to start with? Please input a number between 10 & 100. "))
if choice in range(10,100):
    print("You have chosen {} sticks to start with.".format(choice))
else:
    print("Invalid selection. Please choose again. ")
turn_count = 0
sticks_subtracted = int(input("Please select how many sticks you would like to remove."))
sticks_remaining = choice - sticks_subtracted
if 0 < sticks_subtracted < 4:
    print("There are {} sticks left.".format(sticks_remaining))
else:
    print(int(input("Please select between 1 and 3 sticks. ")))
if sticks_remaining in range(1,100):
    sticks_subtracted = int(input("Please select how many sticks you would like to remove."))
    sticks_remaining = sticks_remaining - sticks_subtracted
    w sticks_remaining > 1:
        print("There are {} sticks left.".format(sticks_remaining))
        sticks_subtracted = int(input("Please select how many sticks you would like to remove."))
    if sticks_remaining == 1:
        print("There are {} sticks left. You lose.".format(sticks_remaining))
    if sticks_remaining < 1:
        print("There are no sticks remaining. You lose.")








    #     print("Not a valid selection. Try again")


#removing sticks
# def remove_sticks:
#



# def player_names():
#     player_1 = input("What is your name, player 1? ")
#     player_2 = input("What is your name, player 2? ")
