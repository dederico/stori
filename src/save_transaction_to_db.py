import sqlite3

def save_transaction_to_database(id, date, transaction):
    connection = sqlite3.connect('transactions.db')
    cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions
                      (id INTEGER PRIMARY KEY,
                      date TEXT,
                      "transaction" TEXT,
                      UNIQUE(id))''')

    try:
        cursor.execute('INSERT INTO transactions (id, date, "transaction") VALUES (?, ?, ?)', (id, date, transaction))
        connection.commit()
        print(f"Transaction with id {id} inserted successfully!")
    except sqlite3.IntegrityError:
        print(f"Transaction with id {id} already exists. Skipping insertion.")

    connection.close()
