import sqlite3

class Shop:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.curser = self.connection.cursor()

    def create_table(self):
        self.curser.execute("""
            CREATE TABLE IF NOT EXISTS shope_data (
                Cid INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                address TEXT NOT NULL,
                total_loan REAL NOT NULL DEFAULT 0,
                deposit_loan REAL NOT NULL DEFAULT 0,
                remaining_Amount REAL NOT NULL DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.connection.commit()

    def get_phone_number(self, id):
        try:
            self.curser.execute("SELECT phone FROM shope_data WHERE Cid = ?", (id,))
            rows = self.curser.fetchall()
            return rows
        except sqlite3.Error as e:
            print(f"An error occurred while fetching phone number: {e}")
            return None

    def close_connection(self):
        if self.curser:
            self.curser.close()
        if self.connection:
            self.connection.close()

# Usage example
shop = Shop('shop_db.db')
shop.create_table()
phone_number = shop.get_phone_number(1)
if phone_number:
    print(f"Phone number: {phone_number}")
else:
    print("Phone number not found or error occurred.")
shop.close_connection()
