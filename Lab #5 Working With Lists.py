# Lab 5: Working with Lists
import csv
import matplotlib.pyplot as plt

data = "top50 songs.csv"
song_idx = 1
artist_idx = 2
streams_idx = 3
genre_idx = 4
energy_idx = 11

def read_records(data):
    with open(data, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader, None)
        return list(reader)

rows = read_records(data)
songs = [r[song_idx] for r in rows]   
artists = [r[artist_idx] for r in rows]   
genres = [r[genre_idx] for r in rows]   

#practice
book = ["song"] * 5
print("Repititon Example: ", book)

print("For Loop Example:")
for s in songs:
    print(s)

print("Len Example:")
print("Number of rows: ", len(songs))

print("Changing List Example: ")
print("Before: ", rows[0][song_idx])
rows[0][song_idx] = rows[0][song_idx] + " :)"
print("After: ", rows[0][song_idx])

print("Slicing Example:")
print("Songs 1 & 2: ", songs[0:2])
print("Songs 3 & 4: ", songs[2:4])

print("In operator: ")
item = "Espresso"
print(item, " in songs?", item in songs)
artist_check = "Sabrina Carpenter"
print(artist_check, "in artists?", artist_check in artists)

print("Only Artist Names:")
for a in artists:
    print(a)

print("Unique Artists: ")
unique_artists = []
seen = set()
for a in artists:
    if a not in seen:
        seen.add(a)
        unique_artists.append(a)
for a in unique_artists:
    print(a)

print("Genre Pie Chart:")
def genre_counts(records, genre_idx):
    counts = {}
    for r in records:
        genre = r[genre_idx]
        if genre == "":
            genre = "Unknown"
        counts[genre] = counts.get(genre, 0) + 1
    return counts
def plot_genre_pie(genre_count_dict):
    labels = list(genre_count_dict.keys())
    sizes = list(genre_count_dict.values())
    plt.figure(figsize=(8,8))
    plt.pie(sizes, labels=labels, startangle=140)
    plt.title("Genre Distribution")
    plt.axis('equal')
    plt.show()
gcounts = genre_counts(rows, genre_idx)
plot_genre_pie(gcounts)

print("Bar Graph of Artists vs Streams:")
def plot_artists_vs_streams_bar(records, artist_idx, streams_idx):
    totals = {}
    for r in records:
        artist = r[artist_idx]
        s = r[streams_idx] 
        streams = float(s)
        totals[artist] = totals.get(artist, 0) + streams
    sorted_totals = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    artists = [a for a, _ in sorted_totals]
    stream = [t for _, t in sorted_totals]
    plt.figure(figsize=(max(10, len(artists) * 0.25), 6))
    bars = plt.bar(artists, stream, color='skyblue')
    plt.xticks(rotation=90, ha='right')
    plt.ylabel('Total Streams')
    plt.title(f'Artists by Total Streams showing {len(artists)}')
    plt.tight_layout()
    plt.show()
plot_artists_vs_streams_bar(rows, artist_idx, streams_idx)

#student activity
def plot_artists_energy_songs(records, song_idx, energy_idx):
    totals = {}
    for r in records:
        song = r[song_idx]
        s = r[energy_idx] 
        energy = float(s)
        totals[song] = totals.get(song, 0) + energy
    sorted_totals = sorted(totals.items(), key=lambda x: x[1], reverse=True)
    songs = [a for a, _ in sorted_totals]
    energys = [t for _, t in sorted_totals]
    plt.figure(figsize=(max(10, len(songs) * 0.25), 6))
    bars = plt.bar(songs, energys, color='skyblue')
    plt.xticks(rotation=90, ha='right')
    plt.ylabel('Total Energy')
    plt.title(f'Highest Energy by Song')
    plt.tight_layout()
    plt.show()
plot_artists_energy_songs(rows, song_idx, energy_idx)
print("The song with the highest energy is good 4 u by Olivia Rodrigo.")