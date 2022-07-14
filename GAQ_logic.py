from csv import DictReader
from GAQ_gameinfo import generate_new_quote

def _quote():
    with open("GAQ_gameinfo.csv" , "r") as csvfile:
        csv_dictreader = DictReader(csvfile)
        for row in csv_dictreader:
            quote = row["Quote"]
            return quote 

def _author():
    with open("GAQ_gameinfo.csv" , "r") as csvfile:
        csv_dictreader = DictReader(csvfile)
        for row in csv_dictreader:
            author = row["Author"]
            return author

def _about():
    with open("GAQ_gameinfo.csv" , "r") as csvfile:
        csv_dictreader = DictReader(csvfile)
        for row in csv_dictreader:
            about = row["About"]
            return about 

def gameplay():
    while True:
        num = 4 
        generate_new_quote()
        while True:
            print("Here's a quote :")
            print(_quote())
            answer = input(f"Who said this ? {num} Guesses remaining : ")
            if answer != _author():
                if num == 4 :
                    print("Here's a hint :")
                    print(_about()) 
                    num -= 1 
                elif num == 3 :
                    print(f"Here's a hint :")
                    print(f"The author's first name starts with {_author()[0]}")
                    num -= 1
                elif num == 2 : 
                    print("Here's a hint :")
                    print(f"The author's last name ends with {_author()[-1]}")
                    num -= 1 
                else:
                    print(f"Sorry, you've run out of guesses. The answer was {_author()}")
                    break
            elif answer == _author():
                print("Congratulations, you guessed it")
                break 
        next_ = str(input("Do you want to play again (y/n) ? "))
        if next_ == "y":
            print("OK then, good luck")
        elif next_ == "n":
            break 
    return "Thank you for playing!!!"


print(gameplay())