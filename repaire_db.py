import sqlite3
import os

# Path to your database
db_path = 'db.sqlite3'

if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        # Manually add the missing column
        cursor.execute("ALTER TABLE payments_payment ADD COLUMN phone_number varchar(20) DEFAULT '';")
        conn.commit()
        print("✅ Success: phone_number column added to payments_payment table.")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("ℹ️ Note: The column already exists.")
        else:
            print(f"❌ Error: {e}")
    finally:
        conn.close()
else:
    print("❌ Error: db.sqlite3 not found in this folder.")