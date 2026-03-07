import sqlite3

def check_creds():
    try:
        con = sqlite3.connect("vote.db")
        cur = con.cursor()
        
        print("--- Election Officer (eofficer) ---")
        cur.execute("SELECT * FROM eofficer")
        rows = cur.fetchall()
        for row in rows:
            print(row)
            
        print("\n--- Booth Officer (boothofficer) ---")
        cur.execute("SELECT * FROM boothofficer")
        rows = cur.fetchall()
        for row in rows:
            print(row)
            
        con.close()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_creds()
