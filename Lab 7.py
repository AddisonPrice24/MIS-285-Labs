#Lab 7: Are You A Movie Buff?

import csv
data = "netflix_titles.csv"
titles_idx = 2
genre_idx = 9

#practice
print("Program One")
with open(data, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        print(row)
        if i >= 4:
            break


print("Program 2")
with open(data, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        listed_in = (row.get('listed_in') or '')
        tokens = [g.strip().lower() for g in listed_in.split(',') if g.strip()]
for i in tokens[:15]:        
    print(row.get('listed_in'), '->', tokens)

print("Program 3")
found = []
with open(data, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        listed_in = (row.get('listed_in') or '')
        tokens = [g.strip().lower() for g in listed_in.split(',') if g.strip()]
        if 'horror movies' in tokens:
            found.append(row)
print("Number of horror movies on Netflix: " + str(len(found)))

print("Program 4")
non_docs = []
with open(data, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        listed_in = (row.get('listed_in') or '')
        tokens = [g.strip().lower() for g in listed_in.split(',') if g.strip()]
        if 'documentaries' not in tokens:
            non_docs.append(row)
print("Number of non-documentaries on Netflix: " + str(len(non_docs)))
for r in non_docs[:10]:
    print(r.get('title'))

print("Program 5")
with open(data, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        title = (row.get('title'))
        print(title.upper())
        if i > 4:
            break

#student activity
print("Student Activity")
input = input("Enter a title to search for: ").strip()
found = False
with open(data, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        title = (row.get('title'))
        if title == input:
            found = True
            break
if found:
    print(input + " is on Netflix.")
else:
    print(input + " is not on Netflix.")