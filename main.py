import random
list=["If 1=3, 2=3, 3=5, 4=4, 5=4 Then, 6=?","Solve: 3+2*(8-3)","What is the highest common factor of the number 30 and 132?","From the number 0 to the number 1000,the letter\'A\'appears only in which number?","Which prime number is closest to 100?"]
list1=["What gets wet when drying?","I am the rare case when today comes before yesterday.What am I?","What english word retains the same pronunciation,even after you take away four of its five letters?","What has a head and a tail,but no body?","I shave everyday,but my beard stays the same.Who am I?"]


def confirmation():
    print("Type \"yes\" to continue or \"no\" to leave")
    yOrn=input()
    if yOrn=="yes":
        bool=True
        return bool
    elif yOrn=="no":
        bool=False
        return bool
    else:
        print("Invalid input")
        bool=False
        return bool


def quiz():
    print("select \"Maths\" or \"Word Riddles\"")
    print("Type m for \"maths\" or r for \"Word Riddles\"")
    MorG=input()
    if MorG=="m":
        mathQuestion=random.choice(list)
        print(mathQuestion)
        userInput=int(input())
        if mathQuestion==list[0]:
            if userInput==3:
                print("Great,You are absolutely right🥳")
            else:
                print("Sorry,Great try👍Good luck next time")
                print("Answer: 3")
                print("Explanation: Because \'six\' has three letters")
        elif mathQuestion==list[1]:
            if userInput==13:
                print("Great,You are absolutely right🥳")
            else:
                print("Sorry,Great try👍Good luck next time")
                print("Answer: 13")
                print("Explanation: 3+2*(8-3)=3+2(5)=3+10=13")
        elif mathQuestion==list[2]:
            if userInput==6:
                print("Great,You are absolutely right🥳")
            else:
                print("Sorry,Great try👍Good luck next time")
                print("Answer: 6")
        elif mathQuestion==list[3]:
            if userInput==1000:
                print("Great,You are absolutely right🥳")
            else:
                print("Sorry,Great try👍Good luck next time")
                print("Answer: 1000")
                print("Explanation: Thousand")
        elif mathQuestion==list[4]:
            if userInput==101:
                print("Great,You are absolutely right🥳")
            else:
                print("Sorry,Great try👍Good luck next time")
                print("Answer: 101")



             
    elif MorG=="r":
        rdQuestion=random.choice(list1)
        print(rdQuestion)
        userInput1=input().upper()
        if rdQuestion==list1[0]:
            if userInput1=="TOWEL":
                print("Great,You are absolutely right🥳")
            else:
                print("Sorry,Great try👍Good luck next time")
                print("Answer: TOWEL")
        elif rdQuestion==list1[1]:
            if userInput1=="DICTIONARY":
                print("Great,You are absolutely right🥳")
            else:
                print("Sorry,Great try👍Good luck next time")
                print("Answer: DICTIONARY")
        elif rdQuestion==list1[2]:
            if userInput1=="QUEUE":
                print("Great,You are absolutely right🥳")
            else:
                print("Sorry,Great try👍Good luck next time")
                print("Answer: QUEUE")
        elif rdQuestion==list1[3]:
            if userInput1=="COIN":
                print("Great,You are absolutely right🥳")
            else:
                print("Sorry,Great try👍Good luck next time")
                print("Answer: COIN")
        elif rdQuestion==list1[4]:
            if userInput1=="BARBER":
                print("Great,You are absolutely right🥳")
            else:
                print("Sorry,Great try👍Good luck next time")
                print("Answer: BARBER")
    else:
        print("Please give valid input")
    
    



def gamingWithNumbers():
    print("come on...definitely U will gonna love this")
    print("Lets start the game")
    print("select a 6 digit number")
    print("Add all the digits in that number")
    print("subtract this number from the number which u selected at starting and assume this number as x")
    print("Imagine any number secretly from 0 to 9")
    input("Type like ,if you like the game")
    print("Great,Continue with the game...")
    print("Add all 6 digits in x without ur secret number")
    print("If your secret number is not present in x then subtract ur secret number from x and add all digits in x")
    print("Tell me the answer u get now in your mind")
    answer=int(input())
    if answer<=9:
        y1=9-answer
        print("your secret number is %d"%y1)
    elif answer <=18 and 9<answer:
        y2=18-answer
        print("your secret number is %d"%y2)
    elif answer<=27 and 18<answer:
        y3=27-answer
        print("your secret number is %d"%y3)
    elif answer<=36 and 27<answer:
        y4=36-answer
        print("your secret number is %d"%y4)
    elif answer<=45 and 36<answer:
        y5=45-answer
        print("your secret number is %d"%y5)
    else:
        print("plz do correctly and try again\n")
    print("That's great")
    print("Thank u for spending ur valuable time\n")

def treasureIsland():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.")
    choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
    if choice1 == "left":
        choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
        if choice2 == "wait":
            choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
            if choice3 == "red":
                print("It's a room full of fire. Game Over.")
            elif choice3 == "yellow":
                print("You found the treasure! You Win!")
            elif choice3 == "blue":
                print("You enter a room of beasts. Game Over.")
            else:
                print("You chose a door that doesn't exist. Game Over.")
        else:
            print("You get attacked by an angry trout. Game Over.")
    else:
        print("You fell into a hole. Game Over.")


print("Hi Guys")
print("welcome to Priya World")
bool=True
while bool==True:
    print("select one from \"Quiz\" or \"Gaming with python\" or \"Treasure Hunt\"")
    print("Type q for \"Quiz\" or g for \"Gaming with python\" or t for \"Treasure Hunt\"")
    qOrg=input()
    if qOrg=="q":
        print("wow... so you are interested in quiz")
        print("Come,Let's make it more interested")
        quiz()
    elif qOrg=="g":
        print("wow... so you are interested in gaming with numbers")
        print("Come,Let's go into magical world...")
        gamingWithNumbers()
    elif qOrg=="t":
        print("wow... so you are interested in Treasure Hunt")
        print("Come,Let's go into magical World...")
        treasureIsland()
    else:
        print("Invalid input")
    bool=confirmation()