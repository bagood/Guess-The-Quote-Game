from csv import DictReader , DictWriter
from random import choice

def generate_new_quote():
    with open("GAQ_Scrape.csv","r") as csvfile:
        csv_dictreader = DictReader(csvfile)
        info = [ [row["Quote"],row["Author"],row["About"]] for row in csv_dictreader ]
        question = choice(info)
        with open("GAQ_gameinfo.csv", "w") as csv_file:
            header = ["Quote","Author","About"]
            csv_dictwriter = DictWriter(csv_file, fieldnames = header)
            csv_dictwriter.writeheader()
            csv_dictwriter.writerow({
                "Quote" : question[0],
                "Author": question[1],
                "About" : question[2]
            })
