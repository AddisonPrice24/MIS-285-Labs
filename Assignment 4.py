#Assignment 4: Search Your Favorite Movie in Netflix Dataset
#imports the csv file
import csv
data = "netflix_titles.csv"
#asks for and stores the user's input in lowercase
query = input("Enter a movie or TV show to search for: ").strip().lower()
#assumes that if the user's input isn't found, it isn't in the dataset
found = False
#opens & reads the csv dataset
with open(data, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        #performs the matching
        title = (row.get('title'))
        #changes all titles to lowercase for case-insensitive matching
        title = title.lower()
        if title == query:
            listed_in = row.get('listed in') or row.get('Listed In') or row.get('genre') or ''
            print("Found!")
            #prints the title, line number, and genre of the user's query
            print("Title:", row.get('title'))
            print("Line number:", i)
            print("Genre/Category:", row.get('listed_in'))
            found = True
            break
#tells the user if their entry isn't on netflix
if not found:
    print(query + " is not on Netflix.")