import random
from unicodedata import decimal

def menuRun():
    menu = {
    1: 'Horse Racing',
    2: 'Guess the Country',
    3: 'Descibe Yourself',
    4: 'Exit',
}
    for i in menu.keys():
        print (i, '--', menu[i] )

    selection = 0
    
    selection = int(input('Enter your choice: '))
    
    print('Enter only a letter!')
        

    if selection == 1:
           HorseRacing()
    elif selection == 2:
           GuessCountry()
    elif selection == 3:
           Describe()
    elif selection == 4:
           Exit()

def HorseRacing():
    print("Betting Odds: 1: Spark(3/1), 2: Mike(3/1), 3: Fast Al(evens)")
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
    
    selection = int(input("Choose a horses' number: "))
    
    bet = int(input("Place your bet: "))


    
    
   


    results = random.choices(nameList, weights=(25, 25, 50), k=1)

    for i in results:
        name = i

    if horses[selection] == name:
        winning = bet * oddsCalculator[name]
        print(f"{name} is the winner, you won ${winning}!")
        menuRun()
    else:
        print(f"{name} is the winner, you lose!")
        menuRun()



def GuessCountry():
    countries = ["England", "Ireland", "Spain"]

    country = random.choice(countries).upper()

    print("Try and guess the eurpean country!")

    for i in country:
        print("_ ")
        print()

    letterUsed = ''               
    chances =  2
    ltrs = len(country)

    while chances != 0:
    
    
        guess = str(input('Enter a letter to guess: ')).upper()

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

        nameD = str(input('Enter your Name: ')).upper()

        for i in nameD:
            nme = words[i]
        print(nme)
        menuRun()


def Exit():
    exit()



menuRun()
