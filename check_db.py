import sqlite3

def check_db(db_path):
    try:
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cur.fetchall()
        print(f"Tables in {db_path}: {tables}")
        for table in tables:
            table_name = table[0]
            cur.execute(f"PRAGMA table_info({table_name});")
            columns = cur.fetchall()
            print(f"Schema for {table_name}: {columns}")
        con.close()
    except Exception as e:
        print(f"Error checking {db_path}: {e}")

if __name__ == "__main__":
    check_db('vote.db')
