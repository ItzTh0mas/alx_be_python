import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server (adjust user & password if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",         # or 'alxuser'
            password="yourpassword"  # replace with your password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            # Debug: confirm resources closed
            # print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
