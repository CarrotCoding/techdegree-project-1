import random

highscore = 0

print("Welcome to the number guessing extravaganza")
print("In this game you can guess as much as you like")
print("Until the magic random number has been found\n")


#creating a function to create the winning number within the game boundaries
def guessing_game():
    # since I wanted the highscore as a global variable but access it locally I kept running into errors
    # I used https://www.programiz.com/python-programming/global-local-nonlocal-variables to find the solution of how to access a global variable
    # This way I can set the highscore to 0 whenever someone starts the game but keep the current highscore while playing the game
    global highscore
    player_choice = 0
    number_of_tries = 0
    winning_number = random.randrange(1, 11)
    #creating the while loop. This will keep running as long as the player's choice does not equal the winning number
    if highscore == 0:
        print("There is no highscore yet, so go ahead and set one!\n")
    while player_choice != winning_number:
        #the error handling in case someone fills in a number outside of the game boundaries, a float or a string
        try:
            player_choice = int(input("Please provide a number between 1 and 10\n"))
            if player_choice > 10 or player_choice < 1:
                raise ValueError
        except:
            print("Oh no! We ran into an issue. Please try again")
        #the game itself. We do not count an error as a try
        else:
            if player_choice > winning_number:
                print("lower!")
                #the counter that increases upon every try
                number_of_tries += 1
            elif player_choice < winning_number:
                print("higher!")
                number_of_tries += 1
            else:
                #the winning conditions are met
                print("Successssss you've won!")
                number_of_tries += 1
                print("It took you {} tries".format(number_of_tries))
                #updating the highscore to the number_of_tries.
                #if highscore is 0 it's set to number of tries
                #if highscore is not 0 we check whether the new attempt is better and then update
                if highscore == 0:
                    highscore = number_of_tries
                elif number_of_tries < highscore:
                    highscore = number_of_tries
                else:
                    print("Sadly you did not beat the highscore of {}".format(highscore))

                #here we ask the user whether they want to continue
                #any input other than Y or y will lead to exiting the while loop
                player_continue = input("Do you want to continue?\n [y]es or [n]o\n")

                if player_continue.lower() == "y":
                    #here we make sure that the new winning_number is never the same winning_number
                    #here we print the current highscore before the new game
                    print("The current highscore is {}".format(highscore))
                    guessing_game()
                else:
                    #here we thank the user for playing if they choose not to continue
                    print("Thank you for playing")

guessing_game()
