import random

def black_jack():
    cards = {"Ace": [1, 11], "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "King": 10, "Queen": 10, "Jack": 10,} # 11 or 1 = Ace .... 10 = King, Jack, Queen
    userList = [] #The list of the deck of the user
    computerList = [] #The list of the deck of the computer

    def random_draw(userA):
        """Takes a random draw for both user and computer"""
        if userA == "user":
            card = random.choice(list(cards.items())) #Random choice of two cards for the user
            if card[0] == "Ace": #If the card is an ace
                return ace_drawn()
            else: return card[1] #If the card is not an ace
        else: #If the one drawing is a computer
            card = random.choice(list(cards.items())) #Random choice of two cards for the user
            if card[0] == "Ace": #If the card is an ace
                if sum(computerList) < 10: computerList.append(1)
                else: computerList.append(11)
            else: computerList.append(card[1]) #If the card is not an ace

    def ace_drawn():
        """If the ace is drawn"""
        while True:
            print(f"Current deck: {userList} = {sum(userList)}")
            try:
                pick = int(input("You have drawn an 'Ace'. Choose between 1 and 11: "))
                if pick == 1 or pick == 11:
                    return pick
                else:
                    print("Invalid input, please try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 11.")
                    
    def user_draw(n): #Function for the user to draw cards
        """To handle the user draw"""
        for _ in range(n):
            userList.append(random_draw("user"))
        print(f"Your deck: {userList} = {sum(userList)}")
            
    user_draw(2) #at the start the user is given two cards

    #First two draw of the computer
    for item in range(2):
        random_draw("computer")

    print(f"Computer's first card: {computerList[1]}") #Shows the first card that the computer has drawn
    print("\n") #For Space

    #First Conditionals to check if the user won already:
    if sum(userList) == 21 and sum(computerList) == 21: return "Tied!" #these two conditionals check at the start if there is already a conclusion
    elif sum(userList) == 21: return "You win!"
   
    #Ask the user if they would want to hit again:
    drawAgain = input("Would you like to hit again? 'y' or 'n': ").lower() 
    while drawAgain == "y": #If they want to keep drawing cards (if not the loop breaks)
        user_draw(1)
        if sum(userList) > 21: return "You lose! Bust!" #If the user draws again and goes over 21 they immediately lose
        drawAgain = input("Would you like to hit again? 'y' or 'n': ").lower()

    print(f"\nYour deck: {userList} = {sum(userList)}") #Prints out the whole list of the user
    #We check and reveal the computer's full deck and if it is less than 17 then it draws again
    print(f"Computer Deck: {computerList} = {sum(computerList)}") #Reveal the computer's card

    #Computer draws again if the deck total is less than 17:
    while sum(computerList) < 17:
        random_draw("computer")
        print(f"\nComputer draws again, New Deck: {computerList} = {sum(computerList)}")
        
    #Conditional to check in the end if the user won, busted, or lost, maybe even tied:
    if sum(computerList) > 21: return "You win! Computer busted!"
    elif sum(computerList) == sum(userList): return "Tied!"
    elif sum(userList) == 21 or sum(userList) > sum(computerList): return "You win!"
    else: return "You lose!"

#Main Loop of the code:
condition = True
while condition: #Asking the user if they want to play a game of blackjack and looping through the question all over again if they do not input a right answer (y or n)
    play = input("\nDo you want to play a game of Blackjack? 'y' or 'n': ").lower()
    condition = True if play == "y" else False  # If the user says yes the function is called if no or any other input it ends the loop
    if condition:
        print(black_jack())
