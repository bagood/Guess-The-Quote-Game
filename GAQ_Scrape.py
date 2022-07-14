import requests 
from bs4 import BeautifulSoup 
from csv import DictWriter , DictReader

with open("GAQ_Scrape.csv", "w") as csvfile :
    header = ["Quote","Author","About"]
    csv_writer = DictWriter(csvfile, fieldnames = header)
    csv_writer.writeheader()
    num = 1 
    while num < 11 :
        response_main = requests.get(f"http://quotes.toscrape.com/page/{num}/")
        soup_main = BeautifulSoup(response_main.text, "html.parser")
        quotes = soup_main.find_all(class_="quote")
        for quote in quotes:
            text = quote.find(class_="text").get_text()
            author = quote.find(class_="author").get_text()
            about_url = quote.find("a")["href"]
            response_side = requests.get(f"http://quotes.toscrape.com{about_url}")
            soup_side = BeautifulSoup(response_side.text, "html.parser")
            author_borndate = soup_side.find(class_="author-born-date").get_text()
            author_bornloc = soup_side.find(class_="author-born-location").get_text()
            author_desc = f"The author was born on {author_borndate}, {author_bornloc}"
            csv_writer.writerow({"Quote" : text,"Author" : author,"About" : author_desc})
        num += 1
