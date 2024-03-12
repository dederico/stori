import sqlite3

def create_database():
    connection = sqlite3.connect('transactions.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions
                      (id INTEGER PRIMARY KEY,
                      date TEXT,
                      "transaction" TEXT)''')

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_database()
