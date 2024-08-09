import mysql.connector
from mysql.connector import Error

connection_params = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '',
    'database': 'crypto_news'
}


def get_crypto_coins():
    try:
        connection = mysql.connector.connect(**connection_params)
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT crypto_key, detail FROM crypto_coin")
        result = cursor.fetchall()

        return result

    except Error as e:
        print(f"Error fetching crypto coins: {e}")
        return []

    finally:
        # Closing the cursor and connection
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()
