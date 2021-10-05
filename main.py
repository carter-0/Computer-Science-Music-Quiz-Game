import db_manager
import random
import time

print("Welcome to the Music Quiz Game")

def try_login():
    username = str(input("\nEnter your username to login: $ "))
    password = str(input(f"Enter your password for \"{username}\": $ "))

    return db_manager.check_login(username, password), username, password

def player_guess():
    print(f"\nArtist Name: {song_artist}")
    print(f"First letter of song: {song_name[:1]}")
    guess = str(input("Your Guess $ "))

    return guess

def nea_exit(username, score):
    ##display current score, update scores db, display top 5 scores from db
    db_manager.submit_to_leaderboard(username, str(score))
    print("\nGame Over!")
    print(f"You got {str(score)}!\n")
    print("Top 5 scores:")
    for i in db_manager.get_top_5():
        print(f"{i[1]}: {i[2]}")
    exit()

logged_in, username, password = try_login()

while not logged_in: ##Infinite loop unitl logged in
    logged_in, username, password = try_login()

print(f"Login Successful - Hello {username}")
score = 0

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