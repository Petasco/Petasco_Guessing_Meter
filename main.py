import random
print("---------------------------------------------------------")
print("~~~~~~~ WELCOME TO PETASCO GUESSING GAME ~~~~~~~~~~~~~~~~")
print("---------------------------------------------------------")

random_num = random.randint(1, 11)
guesses = 0
while True:
    guesses += 1
    user_guess = input("MAKE A GUESS FROM 1 TO 10: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    if int(user_guess) <= int(0) and int(user_guess) >= int(11):
        print("<=`,`,`,`,`,`,`,`,`,`,`,`,=> OOPs! ENTER A NUMBER FROM 1 TO 10 <=`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,=>")
        quit()

    # end the program if the user enter a string
    else:
        print("<=`,`,`,`,`,`,`,`,`,`,`,`,=> OOPs! ENTER A NUMBER NEXT TIME! <=`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,=>")
        continue
    if user_guess == random_num:
        print("CONGRATS, YOU GOT IT")
        break
    else:
        print("<=`,`,`,`,`,`,`,`,`,`,`,`,=> OOPs! YOU GOT IT WRONG! <=`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,=>")
        # the line below is hack the game for the random number
        #print("THE RANDOM NUMBER WAS:", random_num)

    if guesses == 10:
        print("<=`,`,`,`,`,`,`,`,`,`,`,`,=> OOPs! GAME OVER!!! START AGAIN!!! <=`,`,`,`,`,`,`,`,`,`,`,`,`,`,`,=>")
        quit()

print("YOU GOT IT IN", guesses, "GUESSES OUT OF 10")
loss_in_percentage = (guesses/10) * 100
won_in_percentage = 100 - float(loss_in_percentage)
print("YOU ARE " + str(won_in_percentage) + "% IN GUESSING!")