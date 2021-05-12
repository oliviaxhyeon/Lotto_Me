import random

class Lottery:
    def __init__(self):
        self.my_num = set()  # Entered numbers
        self.winning_num = set()  # Winner's numbers.
        self.bonus = set()  

    # Reset numbers.
    def init(self):
        self.winning_num.clear()  
        self.bonus.clear()  
        while len(self.winning_num) < 6:
            self.winning_num.add(random.randrange(1, 50)) 

        while True:
            n = random.randrange(1, 49)
            if not (n in self.winning_num):  
                self.bonus.add(n)
                break

    # Input lottery numbers.
    def insert(self):
        self.my_num.clear()
        while len(self.my_num) < 6:
            print(str([ len(self.my_num) + 1 ]) + "Put your number (1 ~ 49) : ", end = "")
            n = int(input())  
            if (n < 1) or (n > 49) or (n in self.my_num):  # Wrong numbers
                print("You have entered a wrong number or duplicated number. Please try again with a different number.")
                continue
            self.my_num.add(n)  
            print("Entered numbers : " + str(list(self.my_num)))

    # Match entered Lottery numbers.
    def match(self):
        if len(self.my_num) != 6:
            print("Select 2 to check your number.")
            return
        
        self.print()
        self.printMy_num()
        match_num = len(self.winning_num.intersection(self.my_num))
        if match_num == 6:
            print("* Congratulations! You are the winner. *")
        elif match_num == 5 and self.my_num.intersection(self.bonus):
            print("* Congratulations! You won the 2nd place. *")
        elif match_num == 5:
            print("* Congratulations! You won the 3rd place. *")
        elif match_num == 4:
            print("* Congratulations! You won the 4th place. *")
        elif match_num == 3:
            print("* Congratulations! You won the 5th place. *")
        elif match_num == 2 and self.my_num.intersection(self.bonus):
            print("* Congratulations! You won the 6th place. *")
        else:
            print("* Sorry, maybe next time... *")

    # Output my numbers.
    def printMy_num(self):
        print("My numbers : ", end="")
        tmp = list(self.my_num)
        tmp.sort()
        print(tmp)

    # Output this week's numbers.
    def print(self):
        print("This week's numbers : ", end="")
        arr = list(self.winning_num)
        arr.sort()

        print(arr, end="")
        print(" +", list(self.bonus))


print("Starting Lottery numbers generator...")
lottery = Lottery()
lottery.init()
while True: # Start messages
    print("==========================================================")
    print("Please choose one of the followings:")
    print("1. Show winner's numbers of this week.")
    print("2. Enter your lottery numbers.")
    print("3. Generate new lottery numbers.")
    print("4. Match winner's numbers of this week and your numbers.")
    print("5. End program. ")
    print("==========================================================")
    num = int(input())
    if num == 1:
        print("Show winner's number of this week.")
        lottery.print()
    elif num == 2:
        print("Please enter your 6 lottery numbers.")
        lottery.insert()
        lottery.printMy_num()
    elif num == 3:
        print("Generated numbers : ")
        lottery.init()
        lottery.print()
    elif num == 4:
        print("Results : ")
        lottery.match()
    elif num == 5:
        print("Ending program...")
        break
    print()