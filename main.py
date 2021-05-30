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
INTC = 0
INC = 0
COM = 0
FUM = 0
TD = 0
QBR = 0

SACK_LIST = ["Number", "Of", "Sacks", "="]
FUM_LIST = ["Number", "Of", "Fumbles", "="]

GAME_OVER = 1  # 0 = Game over, 1 = Game Not Over

while GAME_OVER == 1:
    PLAYTYPE = input("Please decide the play type. P for Pass, R for Rush, S For Sack, F for fumble :")
    print("You have selected the play type = to", PLAYTYPE)

    if PLAYTYPE == "P":
        PASS_TYPE = input("Is it complete (0), incomplete (1), or intercepted (2)?")
        print("You have selected the pass type = to", PASS_TYPE)
        PASS_ATTEMPTS = PASS_ATTEMPTS + 1

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
            INTC = INTC + 1
            print(INTC)
            print("Thank You")

    if PLAYTYPE == "R":
        CURRENT_RUSH_YARDS = input("How many yards Rushed?")
        RUSH_ATTEMPTS = RUSH_ATTEMPTS + 1
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


def qbr_calc_function(com, pass_attempts, pass_td, intc, pass_yards):
    qbr_pt_1 = ((com/pass_attempts)-0.3)*5
    qbr_pt_2 = ((pass_yards/pass_attempts)-3)*0.25
    qbr_pt_3 = ((pass_td/pass_attempts)*20)+2.375
    qbr_pt_4 = (intc/pass_attempts)*25
    qbr = ((qbr_pt_1 + qbr_pt_2 + qbr_pt_3 - qbr_pt_4)/6)*100
    return qbr


QBR = qbr_calc_function(COM, PASS_ATTEMPTS, PASS_TD, INTC, PASS_YARDS)
QBR = round(QBR, 1)

RSH_YRD_PER_ATT = RUSH_YARDS/RUSH_ATTEMPTS
PASS_YRD_PER_ATT = PASS_YARDS/PASS_ATTEMPTS
INT_PCT = (INTC/PASS_ATTEMPTS) * 100
COMP_PCT = (COM/PASS_ATTEMPTS) * 100
PASS_TD_PCT = (PASS_TD/PASS_ATTEMPTS) * 100

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
print("Number of INT =", INTC)
print("Passing TD Percentage =", PASS_TD_PCT)
print("Interception Percentage =", INT_PCT)
print("-------------------------Rushing Stats-----------------------------")
print("Rushing Attempts =", RUSH_ATTEMPTS)
print("Rushing Yards =", RUSH_YARDS)
print("Rushing Yards Per Attempt =", RSH_YRD_PER_ATT)
print("Rushing TDs =", RUSH_TD)
print("-------------------------Sacks and Fumble Stats--------------------")
print(SACK_LIST[0], SACK_LIST[1], SACK_LIST[2], SACK_LIST[3], SACKS)
print(FUM_LIST[0], FUM_LIST[1], FUM_LIST[2], FUM_LIST[3], FUM)
print("-------------------------Stats Over--------------------------------")
