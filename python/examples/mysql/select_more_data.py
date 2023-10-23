import mysql.connector


def main():
    conn = mysql.connector.connect(
        host = 'localhost',
        database = 'fb_db',
        user = 'foobar',
        password='no secret')

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM person")

    while True:
        if row := cursor.fetchone():
            print(row)

        else:
            break
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()

