import random
from unicodedata import decimal

def menuRun():
    menu = {
    1: 'Horse Racing',
    2: 'Guess the Country',
    3: 'Descibe Yourself',
    4: 'Exit',
}

    print("\n \nWelcome to the menu")
    for i in menu.keys():
        print (i, '--', menu[i] )

    selection = 0
    while True:
            try:
                selection = int(input('Enter your choice: '))

            except ValueError:
                print("This is an unaccepted response, enter a valid value")
                continue
            else:
                break

    
    
        

    if selection == 1:
           HorseRacing()
    elif selection == 2:
           GuessCountry()
    elif selection == 3:
           Describe()
    elif selection == 4:
           Exit()

def HorseRacing():
    print("\n \nBetting Odds: 1: Spark(3/1), 2: Mike(3/1), 3: Fast Al(evens)")
    horses = {
    1: 'Spark',
    2: 'Magic Mike',
    3: 'Fast Al',
    }

    oddsCalculator = {    'Spark': 4 ,
    'Magic Mike': 4 ,
    'Fast Al': 2,
    }
    nameList = list(horses.values())
    while True:
            try:
                selection = int(input("\n \nChoose a horses' number: "))

            except ValueError:
                print("This is an unaccepted response, enter a valid value")
                continue
            else:
                break
    
    while True:
            try:
                bet = int(input("Place your bet: "))

            except ValueError:
                print("This is an unaccepted response, enter a valid value")
                continue
            else:
                break
    


    
    
   


    results = random.choices(nameList, weights=(25, 25, 50), k=1)

    for i in results:
        name = i

    if horses[selection] == name:
        winning = bet * oddsCalculator[name]
        print(f"{name} is the winner, you won ${winning}!\n \n")
        menuRun()
    else:
        print(f"{name} is the winner, you lose!\n \n")
        menuRun()



def GuessCountry():
    countries = ["England", "Ireland", "Spain"]

    country = random.choice(countries).upper()

    print("\n \nTry and guess the country!")

    for i in country:
        print("_ ")
        print()

    letterUsed = ''               
    chances =  2
    ltrs = len(country)

    while chances != 0:
    
        while True:
            try:
                guess = str(input('Enter a letter to guess: ')).upper()

            except:
                print("This is an unaccepted response, enter a valid value")
                continue
            else:
                break
        

        if guess in country:
            k = country.count(guess) 
            for _ in range(k):   
                letterUsed += guess
                ltrs -= 1 
        else:
            chances -= 1
    
        for i in country:
                if i in letterUsed:
                    print(i, " ") 
                else:
                    print('_ ')
    
        if chances == 0:

            print("You lose")
            menuRun()
        elif ltrs == 0:
            print("The Country is:", country, "Congratulations")
            menuRun()
    
           

def Describe():
    words = {"A": "Amazing",
"B": "Bold",
"C": "Couragous",
"D": "Daring",
"E": "Extravagent",
"F": "Fine",
"G": "Gourgous",
"H": "Holy",
"I": "Intimadating",
"J": "Joyful",
"K": "Knowledgable",
"L": "Loud",
"M": "Meaningless",
"N": "Notable",
"O": "Outstanding",
"P": "Pretty",
"Q": "Quality",
"R": "Resourceful",
"S": "Sound",
"T": "Timid",
"U": "Understanding",
"V": "Vivid",
"W": "Wasteful",
"X": "",
"Y": "",
"Z": "",}
        
    nameD = str(input('\n \nEnter your Name: ')).upper()

    for i in nameD:
        nme = words[i]
        print(nme)
    menuRun()


def Exit():
    exit()



menuRun()
