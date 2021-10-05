# Music Quiz Game - Computer Science NEA

### Structure:

This project is broken down into 3 files:
* main.py
* db_manager.py
* nea.db

### main.py:

main.py is where the game logic can be found. It's the file that is run in order to start the game, and contains the startup and shutdown logic.

The first thing that happens in this file is try_login() is called.

```
def try_login():
    username = str(input("\nEnter your username to login: $ "))
    password = str(input(f"Enter your password for \"{username}\": $ "))

	return db_manager.check_login(username, password), username, password
```

This function queries the SQL database using the db_manager file to check if the login is valid. The returned variables are assigned as can be seen below, and used to check if the user is authenticated:

```
logged_in, username, password = try_login()

while not logged_in: ##Infinite loop unitl logged in
    logged_in, username, password = try_login()
```

If the user enters the correct login information, they are welcomed, and the variable `score` is initialised

```
print(f"Login Successful - Hello {username}")
score = 0
```

This is where the main game loop begins:

```
while True: ##Initialize main game loop
    all_songs = db_manager.get_songs()
    song = random.choice(all_songs) ##var song is tuple with structure (id, 'song1', 'artist1')

    song_name = song[1]
    song_artist = song[2]
    first_letters = []

    if player_guess().lower() != song_name.lower(): ##First Attempt
        print("\nincorrect! 1 attempt left")
        time.sleep(1)
        if player_guess().lower() != song_name.lower(): ##Second Attempt
            nea_exit(username, score)
        else:
            score += 1
            print("\ncorrect! +1 score")
    else:
        score += 2
        print("\ncorrect! +2 score")
```

In the first line of the loop, `all_songs` is assigned to a nested list from the database, containing all of the songs and artists.

A random song is chosen with 

```
song = random.choice(all_songs)
```

From this, the `song_name`, `song_artist` and `first_letters` lists are initialised

```
song_name = song[1]
song_artist = song[2]
first_letters = []
```

From this point, `player_guess()` is called in an `if` statement:

```
def player_guess():
    print(f"\nArtist Name: {song_artist}")
    print(f"First letter of song: {song_name[:1]}")
    guess = str(input("Your Guess $ "))

    return guess
```

This function is just to prevent repeating code, and queries the user for their guess based on the first letter and artist name of the song.

string indicies are used with `song_name[:1]` to get the first letter of the string

back to the if statement:

```
if player_guess().lower() != song_name.lower():
```

here the player guess to compared with the song name to check if they are the same.
if they are, 2 score is added for being the first guess:

```
else:
    score += 2
    print("\ncorrect! +2 score")
```

however if it's not, 