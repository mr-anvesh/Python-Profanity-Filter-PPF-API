import mysql.connector as t
    
# Function to read words from a text file
def read_words_from_file(file_path):
    with open(file_path, 'r') as file:
        words = [line.strip() for line in file]
    return words

# Function to insert words into the MySQL table
def insert_words_into_db(words):
    try:
        # Connect to MySQL database
        connection = t.connect(
            host='localhost',  # Change to your MySQL host
            user='root',  # Change to your MySQL username
            password='password',  # Change to your MySQL password
            database='db_name'  # Change to your MySQL database
        )

        cursor = connection.cursor()

        # Insert words into the table
        for word in words:
            try:
                cursor.execute("INSERT INTO profanitywords (word) VALUES (%s)", (word,))
                #Change the name of table 'profanitywords' and column 'word' accordingly 
            except t.IntegrityError:
                print(f"Word '{word}' is already in the database. Skipping.")

        # Commit the transaction
        connection.commit()

    except t.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    file_path = 'badwords.txt'  # Change to the path of your .txt file
    words = read_words_from_file(file_path)
    insert_words_into_db(words)
