#___________ Mastermind game _____________
play_another_game="yes"
while (play_another_game == "yes"):
    # Input the name of the player
    student_name=input("Please enter your name: ")
    print("___________________________________________________________________________________________________________________________________________")
    print("                                                 " "Hi", student_name, "Welcome to Mastermind !!")
    print("___________________________________________________________________________________________________________________________________________")
    print("\n")
    print("         Number to Guess - X X X X ",end="                                ")
    print("Colour Mapping : (1) - White  (2) - Blue  (3) - Red ")
    print("                                                                                    (4) - Yellow (5) - Green (6) - Purple") 
    print("\n")
    print("         Enter a four digit number.",end="")
    print("                                         Results: Correct colour and position (1)")
    print("                                                                                     Correct colour in the wrong postion (0)")
    print("                                                                                     Incorrect guess (-)")
    print("\n")
    print("___________________________________________________________________________________________________________________________________________")
    #Initializing variables.
    hidden_peg=[]
    attempts=0
    score=100
    guessed_peg=[]
    num1=0
    num2=0
    num3=0
    num4=0
    
    #Importing the function random to generate random numbers.
    import random
    #Generating the hidden peg
    num1=random.randint(1,6)
    num2=random.randint(1,6)
    num3=random.randint(1,6)
    num4=random.randint(1,6)

    #Inserting all four digits to the hidden_peg list
    hidden_peg.append(num1)
    hidden_peg.append(num2)
    hidden_peg.append(num3)
    hidden_peg.append(num4)
    #print(hidden_peg)
    
    print("         Attempt No",end="")
    print("                                  Guess",end="           ")
    print("                     Result")
    print("___________________________________________________________________________________________________________________________________________")

    while attempts < 8:
        chances=attempts+1
        print("\n")
        print("            ",chances,end="                                       ")
        
        # Entering the player guess
        guess=input("")
        digit1,digit2,digit3,digit4=guess
              

        #Converting player guess into inetger. 
        digit1=int(digit1)
        digit2=int(digit2)
        digit3=int(digit3)
        digit3=int(digit4)


        #Inserting all four digits to the guessed_peg list.
        guessed_peg.append(digit1)
        guessed_peg.append(digit2)
        guessed_peg.append(digit3)
        guessed_peg.append(digit4)
  
        
        #Teminate the game without going to the 8th guess
        if guessed_peg == "0000":
            print("game ended.")
            break
                  
        #Checking whether the guessed peg is correct.
        if guessed_peg == hidden_peg:
            print("Congratulation you won the game.")
            score = score - 12.5*attempts
            print("You have scored ",score,"points.")
            break
        
        #Initializing variables
        option1=""
        option2=""
        option3=""
        option4=""

        # Comparing each elememt in hidden peg and guessed peg.
        if guessed_peg[0] == hidden_peg[0]:
            option1="1"
        elif guessed_peg[0] in hidden_peg:
            option1="0"
        else:
            option1="-"  

        if guessed_peg[1] == hidden_peg[1]:
            option2="1"
        elif guessed_peg[1] in hidden_peg:
            option2="0"
        else:
            option2="-"   

        if guessed_peg[2] == hidden_peg[2]:
            option3="1"
        elif guessed_peg[2] in hidden_peg:
            option3="0"
        else:
            option3="-"  

        if guessed_peg[3] == hidden_peg[3]:
            option4="1"
        elif guessed_peg[3] in hidden_peg:
            option4="0"
        else:
            option4="-"  

        # If the player ran out of guesses.
        if chances >= 8:
            print("\n")
            print("No more attempts.")
            print("You have scored 0 points.")
            break

       #Clearing list to restart the game
        guessed_peg=[]
        attempts=attempts+1

        #Printing the results 
        print("_____________________________________________________________________________________________",option1,option2)
        print("                                                                                             ",option3,option4)
    print("_____________________________________________________________________________________________________________________________________________")    
    play_another_game ="no"
    print("\n")
    play_another_game = str(input("Do you want to play another game (yes/no)? "))
    continue
print("Thankyou for playing the game.")

    

    









    
