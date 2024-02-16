#9. Song Organizer:
# Develop a program that stores song titles, artists, and genres in a dictionary. Include functions to 
#sort by different criteria (title, artist, genre) and search for specific songs

def add_song(library, title, artist, genre):
    library[title] = {'artist': artist, 'genre': genre}
    print(f"\nSong '{title}' by {artist} added to the library.")

def sort_songs(library, key):
    sorted_songs = sorted(library.items(), key=lambda x: x[1][key])
    return dict(sorted_songs)

def search_song(library, query):
    matching_songs = {title: details for title, details in library.items() if query.lower() in title.lower()}
    
    if matching_songs:
        print("\nMatching Songs:")
        for title, details in matching_songs.items():
            print(f"{title} by {details['artist']} ({details['genre']})")
    else:
        print(f"No songs found matching '{query}'.")

def main():
    song_library = {}

    while True:
        print("\nOptions:")
        print("1. Add Song")
        print("2. Sort Songs")
        print("3. Search for Song")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            title = input("Enter the song title: ")
            artist = input("Enter the artist: ")
            genre = input("Enter the genre: ")
            add_song(song_library, title, artist, genre)

        elif choice == '2':
            sort_key = input("Enter the sorting criteria (title, artist, genre): ").lower()
            if sort_key in ['title', 'artist', 'genre']:
                sorted_library = sort_songs(song_library, sort_key)
                print("\nSorted Songs:")
                for title, details in sorted_library.items():
                    print(f"{title} by {details['artist']} ({details['genre']})")
            else:
                print("\nInvalid sorting criteria. Please enter title, artist, or genre.")

        elif choice == '3':
            search_query = input("Enter the song title or part of the title to search: ")
            search_song(song_library, search_query)

        elif choice == '4':
            print("\nExiting the program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()