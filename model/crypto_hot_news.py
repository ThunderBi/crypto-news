import mysql.connector
from mysql.connector import Error

connection_params = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '',
    'database': 'crypto_news'
}


def insert_hot_news(title, body, url, channel):
    try:
        connection = mysql.connector.connect(**connection_params)
        cursor = connection.cursor()
        query = "INSERT INTO crypto_hot_news (title, body, url, channel) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (title, body, url, channel))
        connection.commit()
        print('Data inserted successfully')
    except Error as e:
        print(f"Error: {e}")
    finally:
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()


def get_crypto_coins_by_detail(url):
    try:
        connection = mysql.connector.connect(**connection_params)
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM crypto_hot_news WHERE url = %s", (url,))
        result = cursor.fetchone()

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
