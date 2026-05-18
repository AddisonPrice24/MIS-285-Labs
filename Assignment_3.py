# Assignment #3: Spotify Dataset Analysis
import csv
import matplotlib.pyplot as plt
data = "spotify_alltime_top100_songs.csv"

def read_records(data):
    records = []
    with open(data, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader, None)
        for row in reader:
            if row:
                records.append(row)
    return records

def unique_artists(records, artist_idx):
    seen = set()
    unique = []
    for r in records:
        artist = r[artist_idx]
        if artist not in seen:
            seen.add(artist)
            unique.append(artist)
    return unique

def artist_search(records, artist_idx, query):
    count = 0
    matches = []
    q = query.lower()
    for r in records:
        artist = r[artist_idx]
        if q in artist.lower():
            count += 1
            matches.append(artist)
    return count, matches

def genre_counts(records, genre_idx):
    counts = {}
    for r in records:
        genre = r[genre_idx]
        if genre == "":
            genre = "Unknown"
        counts[genre] = counts.get(genre, 0) + 1
    return counts

def plot_genre_pie(genre_count):
    labels = list(genre_count.keys())
    sizes = list(genre_count.values())
    plt.figure(figsize=(8,8))
    plt.pie(sizes, labels=labels, startangle=140)
    plt.title("Genre Distribution")
    plt.axis('equal')
    plt.show()


def main():
    records = read_records(data)
    if not records:
        print("No data found in", data)
        return
    ARTIST_IDX = 2
    GENRE_IDX = 4
    uniques = unique_artists(records, ARTIST_IDX)
    print("Unique artists:")
    for a in uniques:
        print(a)
    print()

    query = input("Enter artist name: ")
    count, matches = artist_search(records, ARTIST_IDX, query)
    if count > 0:
        print(f"{query} appears {count} times in the chart.")
    else:
        print(f"{query} does not appear in the chart.")
    print()
    gcounts = genre_counts(records, GENRE_IDX)
    print("Genre counts:")
    for g, c in sorted(gcounts.items(), key=lambda x: x[1], reverse=True):
        print(f"{g} : {c}")
    print()
    plot_genre_pie(gcounts)

if __name__ == "__main__":
    main()