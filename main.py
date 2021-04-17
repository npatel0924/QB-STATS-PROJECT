print("This project was made by Nikunj Patel for AP Computer Science Principles.")
print("This program allows the user to input statistics for a quarterback in a game of football and outputs all basic")
print("and advanced statistics once the program is done running.")

QB_NAME = input("What is the QB's name?")
print(QB_NAME)
RUSH_ATTEMPTS = 0
PASS_ATTEMPTS = 0
PASS_YARDS = 0
CURRENT_PASS_YARDS = 0
RUSH_YARDS = 0
CURRENT_RUSH_YARDS = 0
PASS_TD = 0
RUSH_TD = 0
SACKS = 0
SS = 0
INT = 0
INC = 0
COM = 0
FUM = 0
TD = 0
RSH_YRD_PER_ATT = 0
PASS_YRD_PER_ATT = 0
INT_PCT = 0
COMP_PCT = 0
PASS_TD_PCT = 0
QBR = 0

GAME_OVER = 1  # 0 = Game over, 1 = Game Not Over

while GAME_OVER == 1:
    PLAYTYPE = input("Please decide the play type. P for Pass, R for Rush, S For Sack, F for fumble :")
    print("You have selected the play type = to", PLAYTYPE)

    if PLAYTYPE == "P":
        PASS_TYPE = input("Is it complete (0), incomplete (1), or intercepted (2)?")
        print("You have selected the pass type = to", PASS_TYPE)

        if PASS_TYPE == "0":
            CURRENT_PASS_YARDS = input("How many yards passed? :")
            PASS_YARDS = int(CURRENT_PASS_YARDS) + int(PASS_YARDS)
            print("New value of total passing yards for this QB is :", PASS_YARDS)
            COM = COM + 1
            DID_SCORE = input("Did QB score touchdown? Y/N :")

            if DID_SCORE == "Y":
                TD = TD + 1
                PASS_TD = PASS_TD + 1
                print("Passing TD and total TDs has been increased to ", PASS_TD, "and", TD)
            else:
                print("Passing TD and total TDs has not been increased")

        if PASS_TYPE == "1":
            print("Incomplete")
            INC = INC + 1
            print(INC)
            print("Thank You")

        if PASS_TYPE == "2":
            print("Intercepted")
            INT = INT + 1
            print(INT)
            print("Thank You")

    if PLAYTYPE == "R":
        CURRENT_RUSH_YARDS = input("How many yards Rushed?")
        RUSH_YARDS = int(CURRENT_RUSH_YARDS) + int(RUSH_YARDS)
        print(RUSH_YARDS)
        DID_SCORE = input("Did QB Score? Y/N")

        if DID_SCORE == "Y":
            TD = TD + 1
            print(TD)
            print("Thank You")
        else:
            print(TD)
            print("Thank You")

    if PLAYTYPE == "F":
        SS = input("Was it a strip sack? Y/N")

        if SS == "Y":
            SACKS = SACKS + 1
            FUM = FUM + 1
            print(FUM)
            print(SACKS)
            print("Thank You")

        if SS == "N":
            SACKS = SACKS + 1
            print(SACKS)
            print("Thank You")

    if PLAYTYPE == "S":
        SACKS = SACKS + 1
        print(SACKS)
        print("Thank You")
    GAME_OVER = int(input("Is game over. Please type 1 for no and 0 for yes: "))
    print(GAME_OVER)

print("Game is over")
print("Please read the QB stats below for", QB_NAME)
print("-------------------------Passing Stats-----------------------------")
print("Passer Rating = ", QBR)
print("Completions =", COM)
print("Passing Attempts", PASS_ATTEMPTS)
print("Completion Percentage =", COMP_PCT)
print("Passing Yards =", PASS_YARDS)
print("Yards Per Attempt =", PASS_YRD_PER_ATT)
print("Number of Passing TDs =", PASS_TD)
print("Number of INT =", INT)
print("Passing TD Percentage =", PASS_TD_PCT)
print("Interception Percentage =", INT_PCT)
print("-------------------------Rushing Stats-----------------------------")
print("Rushing Attempts =", RUSH_ATTEMPTS)
print("Rushing Yards =", RUSH_YARDS)
print("Rushing Yards Per Attempt =", RSH_YRD_PER_ATT)
print("Rushing TDs =", RUSH_TD)
print("-------------------------Sacks and Fumble Stats--------------------")
print("Number Of Sacks =", SACKS)
print("Number Of Fumbles Lost =", FUM)
print("-------------------------Stats Over--------------------------------")
