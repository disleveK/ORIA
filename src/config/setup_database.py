import sqlite3

def setup_database():
    """
    Create a SQLite database schema for storing documents and metadata.
    """
    conn = sqlite3.connect("oria.db")
    cursor = conn.cursor()

    # Create Documents table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        content TEXT
    )
    ''')

    # Create Metadata table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Metadata (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        document_id INTEGER,
        cancer_types TEXT,
        drugs TEXT,
        FOREIGN KEY(document_id) REFERENCES Documents(id)
    )
    ''')

    conn.commit()
    conn.close()
    print("Database setup completed.")

if __name__ == "__main__":
    setup_database()