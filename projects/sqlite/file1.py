import sqlite3

def main():
    conn = sqlite3.connect("/home/whoami/Documents/project_vscode/python/projects/sqlite/example.db")
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS fish")
    conn.commit()
    
    cursor.execute("CREATE TABLE fish (name TEXT, species TEXT, age INTEGER)")
    cursor.execute("INSERT INTO fish VALUES ('Nemo', 'Clownfish', 2)")
    cursor.execute("INSERT INTO fish VALUES ('Sammy', 'shark', 1)")
    cursor.execute("INSERT INTO fish VALUES ('Jamie', 'cuttlefish', 7)")
    rows = cursor.execute("SELECT * FROM fish").fetchall()
    print(rows)
    conn.commit()
    conn.close()


if  __name__ == "__main__":
    main()