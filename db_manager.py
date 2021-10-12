import sqlite3

def check_login(username, password): ##checks for username and password combo in sqlite database
    conn = sqlite3.connect('nea.db')
    c = conn.cursor()

    c.execute("SELECT * FROM logins WHERE username = ? AND password = ?", (username, password)) ##SQL query is executed
    rows = c.fetchall()
    conn.close()

    if len(rows) == 0: ##var rows contains all instances of matching usr:pass combos therefore if the length = 0, the login is incorrect
        return False
    else:
        return True

def get_songs(): ##return nested list of all song names and artists
    conn = sqlite3.connect('nea.db')
    c = conn.cursor()

    c.execute("SELECT * FROM songs")
    rows = c.fetchall()
    conn.close()

    return rows

def submit_to_leaderboard(username, score): ##add score to leaderboard table
    conn = sqlite3.connect('nea.db')
    c = conn.cursor()

    c.execute("SELECT * FROM leaderboard WHERE username = ?", (username,))
    rows = c.fetchall()

    if len(rows) == 0:
        c.execute("INSERT INTO leaderboard(username, score) VALUES(?, ?)", (username, str(score)))
    else:
        if int(score) < int(rows[0][2]):
            conn.close()
            return
        else:
            c.execute("UPDATE leaderboard SET score = ? WHERE username = ?", (str(score), username))

    conn.commit()
    conn.close()

def get_top_5(): ##returns top 5 from leaderboard in nested list
    conn = sqlite3.connect('nea.db')
    c = conn.cursor()

    c.execute("SELECT * FROM leaderboard ORDER BY -ABS(score) LIMIT 5") ##SQL: top 5 ordered by score descending
    rows = c.fetchall()

    return rows