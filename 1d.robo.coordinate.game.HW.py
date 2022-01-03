from os import system
# a - move left
# d - move right

length  = range(1,21)
roboX   = 5

bomb1X  = 8
bomb2X  = 19
bomb3X  = 14

heart1X = 2
heart2X = 12
heart3X = 17

hp      = 100

limitL  = 0
limitR  = 21

charge  = 100

score   = 0

money1X = 7
money2X = 10
money3X = 16


while True:
    system("cls")

    # ##################  INTERACTION WITH BOMBS  ###########
    if roboX == bomb1X or roboX == bomb2X or roboX == bomb3X:
       hp -= 50
    # #######################################################

    # ##################  INTERACTION WITH HEARTS  ##########
    if hp < 100:
       if (roboX == heart1X or roboX == heart2X or roboX == heart3X) and hp != 90:
          hp += 20
       elif (roboX == heart1X or roboX == heart2X or roboX == heart3X) and hp == 90:
           hp += 10
     
    # ##################  CONDITION OF LOSING IN THE GAME  ##
    if hp <= 0 or charge == 0:
       print("❌❌❌ GAME OVER :( ❌❌❌")
       break
    # ########################################################

    # ##################  DRAWING THE MAP  ###################
    x = 1
    print("\n")

    for x in length:
        if x == roboX:
            print("😶", end = "")  
        elif x == bomb1X or x == bomb2X or x == bomb3X:
            print("💣", end = "")
        elif x == heart1X or x == heart2X or x == heart3X:
            print("♥", end = "")
        elif x == money1X or x == money2X or x == money3X:
            print("💰", end = "")
        else:
            print("▬", end = "")   
        x += 1

    print("\n")

    print("Health points: ", hp, " %")
    print("Battery level: ", charge, " %")
    print("Score: ", score, " points")
    # #########################################################

    # ##################  CONTROLS  ###########################
    direction = input("dir (a/d/x) > ")
    
    if direction == "a":
        roboX -= 1
    if direction == "d":
        roboX += 1
    if direction == "x":
        system("cls")
        print("Thank you for playing!!!")
        break
    # #########################################################

    # ##################  BORDERS a) teleport ############################
#    if roboX == limitL:              
#        roboX = 20
#    if roboX == limitR:
#        roboX = 1
    # ####################################################################

    # ##################  BORDERS a) stop ################################
    if roboX == limitL:
        roboX = 1
    if roboX == limitR:
        roboX = 20
    # ####################################################################

    # ##################  BATTERY  #######################################
    if direction == "a" or direction == "d":
        charge -= 5
    # ####################################################################

    # ##################  SCORE GAINING  #################################
    if roboX == money1X or roboX == money2X or roboX == money3X:
        score += 10
    # ####################################################################