import mysql.connector
from mysql.connector import Error

def create_database():
    """
    Create the alx_book_store database in MySQL server.
    Handles connection errors and checks if database already exists.
    """
    connection = None
    cursor = None
    
    try:
        # Establish connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',  # Update with your MySQL password if needed
            port=3306
        )
        
        # Create cursor to execute queries
        cursor = connection.cursor()
        
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        connection.commit()
        
        print("Database 'alx_book_store' created successfully!")
        
    except Error as e:
        # Handle connection and query errors
        if e.errno == 2003:
            print("Error: Unable to connect to MySQL server. Please ensure MySQL is running.")
        elif e.errno == 1045:
            print("Error: Invalid username or password.")
        else:
            print(f"Error: {e}")
    
    finally:
        # Close cursor and connection
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
