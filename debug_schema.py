import sqlite3

def check_voter_schema():
    con = sqlite3.connect('vote.db')
    cur = con.cursor()
    cur.execute("PRAGMA table_info(Voter);")
    columns = cur.fetchall()
    for col in columns:
        print(col)
    con.close()

if __name__ == "__main__":
    check_voter_schema()
